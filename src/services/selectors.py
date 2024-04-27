from typing import Iterable

from services.models import Service


def service_list(category_id: int | None = None) -> Iterable[Service]:
    queryset = Service.objects.select_related("category")

    if category_id:
        queryset = queryset.filter(category_id=category_id)

    return queryset.all()
