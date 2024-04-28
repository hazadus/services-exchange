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


def project_get_by_id(project_id: int) -> Project | None:
    return (
        Project.objects.filter(id=project_id)
        .select_related("category__parent__parent")
        .select_related("customer")
        .first()
    )
