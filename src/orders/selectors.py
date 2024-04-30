from django.db.models import Q, QuerySet

from orders.models import Order


def order_list(user_id: int) -> QuerySet:
    """Выбирает заказы, где пользователь с user_id заказчик или исполнитель."""
    orders = Order.objects.filter(Q(customer_id=user_id) | Q(provider_id=user_id)).all()
    return orders
