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
