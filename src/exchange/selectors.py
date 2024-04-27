from typing import Iterable

from exchange.models import Category


def category_list() -> Iterable[Category]:
    return (
        Category.objects.prefetch_related("parent")
        .prefetch_related("parent__parent")
        .prefetch_related("subcategories")
        .prefetch_related("subcategories__subcategories")
        .all()
    )
