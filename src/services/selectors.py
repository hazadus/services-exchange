from typing import Iterable

from services.models import Service


def service_list(category_id: int | None = None) -> Iterable[Service]:
    queryset = Service.objects.select_related("category")

    if category_id:
        queryset = queryset.filter(category_id=category_id)

    return queryset.all()


def service_get_by_id(service_id: int) -> Service | None:
    return (
        Service.objects.filter(id=service_id)
        .select_related("category__parent__parent")
        .select_related("provider")
        .first()
    )
