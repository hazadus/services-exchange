from typing import Iterable

from django.db.models import QuerySet

from exchange.models import Category


def category_list() -> QuerySet:
    return (
        Category.objects.prefetch_related("parent")
        .prefetch_related("parent__parent")
        .prefetch_related("subcategories")
        .prefetch_related("subcategories__subcategories")
        .all()
    )


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
