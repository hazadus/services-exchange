from django.db.models import QuerySet

from services.models import Service


def service_list(
    category_id: int | None = None, provider_id: int | None = None
) -> QuerySet:
    queryset = Service.objects.select_related(
        "category", "category__parent", "category__parent__parent", "provider"
    )

    if category_id:
        queryset = queryset.filter(category_id=category_id)

    if provider_id:
        queryset = queryset.filter(provider_id=provider_id)

    return queryset.all()


def service_get_by_id(service_id: int) -> Service | None:
    return (
        Service.objects.filter(id=service_id)
        .select_related("category__parent__parent")
        .select_related("provider")
        .first()
    )
