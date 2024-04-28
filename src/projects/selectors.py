from django.db.models import QuerySet

from projects.models import Project


def project_list(
    category_id: int | None = None, customer_id: int | None = None
) -> QuerySet:
    queryset = Project.objects.select_related("category", "customer")

    if category_id:
        queryset = queryset.filter(category_id=category_id)

    if customer_id:
        queryset = queryset.filter(customer_id=customer_id)

    return queryset.all()
