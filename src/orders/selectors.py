from django.db.models import Q, QuerySet

from orders.models import Order


def order_list(user_id: int) -> QuerySet:
    """Выбирает заказы, где пользователь с user_id заказчик или исполнитель."""
    orders = Order.objects.filter(Q(customer_id=user_id) | Q(provider_id=user_id)).all()
    return orders


def order_list_as_customer(user_id: int) -> QuerySet:
    return Order.objects.filter(customer_id=user_id).all()


def order_list_as_provider(user_id: int) -> QuerySet:
    return Order.objects.filter(provider_id=user_id).all()


def order_get_by_id(order_id: int) -> Order | None:
    return Order.objects.filter(id=order_id).first()
