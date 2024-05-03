from django.contrib.contenttypes.models import ContentType
from django.db.models import QuerySet
from orders.models import Order

from exchange.models import Category, Chat, Message


def category_list() -> QuerySet:
    return Category.objects.prefetch_related(
        "parent", "parent__parent", "subcategories", "subcategories__subcategories"
    ).all()


def category_list_only_available() -> QuerySet:
    """Возвращает только категории, доступные для назначения услугам и проектам –
    то есть не имеющие подкатегорий."""
    return category_list().filter(subcategories=None).all()


def category_get_by_id(category_id: int) -> Category | None:
    return (
        Category.objects.filter(id=category_id)
        .prefetch_related("parent")
        .prefetch_related("parent__parent")
        .first()
    )


def message_list_for_topic(topic: Order) -> QuerySet:
    """Выбирает все сообщения из чата, связанноого с указанной "темой"."""
    chat = Chat.objects.filter(
        topic_ct=ContentType.objects.get_for_model(topic), topic_id=topic.pk
    ).first()
    return Message.objects.filter(chat=chat).order_by("created").all()
