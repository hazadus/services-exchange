from django.contrib.contenttypes.models import ContentType
from projects.models import Project
from services.models import Service
from users.models import Action, CustomUser
from users.services import action_create

from orders.models import Order


def order_create(
    customer: CustomUser,
    provider: CustomUser,
    item: Service | Project,
    price: int,
    comment: str | None = None,
) -> Order:
    """Создаёт заказ на услугу или проект, и соответствующее действие (Action) пользователя."""
    order = Order(
        customer=customer,
        provider=provider,
        item_ct=ContentType.objects.get_for_model(item),
        item_id=item.pk,
        price=price,
        comment=comment,
    )
    order.save()

    # Создадим соответствующие действия для заказчика и исполнителя
    action_create(customer, verb=Action.PLACE_ORDER, target=order)
    action_create(provider, verb=Action.RECEIVE_ORDER, target=order)

    return order


def order_set_status(order: Order, new_status: str, actor: CustomUser) -> None:
    """Изменяет статус заказа на указанный (если это возможно) и создаёт соответствующее действие
    пользователя с этим заказом."""
    match new_status:
        case "cancelled_by_customer":
            # Заказчик может отменить заказ, только если он ещё не был принят в работу исполнителем
            if (order.status == "created") and (actor == order.customer):
                order.status = "cancelled_by_customer"
                order.is_cancelled = True
                order.save()
                action_create(user=actor, verb=Action.CANCEL_ORDER, target=order)
        case "rejected_by_provider":
            # Исполнитель может отклонить заказ, пока он только создан заказчиком:
            if (order.status == "created") and (actor == order.provider):
                order.status = "rejected_by_provider"
                order.is_cancelled = True
                order.save()
                action_create(user=actor, verb=Action.REJECT_ORDER, target=order)
        case "in_progress":
            if (order.status == "created") and (actor == order.provider):
                order.status = "in_progress"
                order.save()
                action_create(user=actor, verb=Action.ACCEPT_ORDER, target=order)
        case "submitted_by_provider":
            # Исполнитель может "сдать" заказ находящийся в работе
            if (order.status == "in_progress") and (actor == order.provider):
                order.status = "submitted_by_provider"
                order.save()
                action_create(user=actor, verb=Action.SUBMIT_ORDER, target=order)
        case _:
            return None
