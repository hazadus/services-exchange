from django.db.models import Count, Q, QuerySet
from users.models import CustomUser

from projects.models import Offer, Project


def project_list(
    category_id: int | None = None, customer_id: int | None = None
) -> QuerySet:
    queryset = Project.objects.select_related(
        "category", "category__parent", "category__parent__parent", "customer"
    ).annotate(offer_count=Count("offers", filter=Q(offers__is_cancelled=False)))

    if category_id:
        queryset = queryset.filter(category_id=category_id)

    if customer_id:
        queryset = queryset.filter(customer_id=customer_id)

    return queryset.all()


def project_get_by_id(project_id: int) -> Project | None:
    return (
        Project.objects.filter(id=project_id)
        .select_related("category__parent__parent", "customer")
        .prefetch_related("offers", "offers__candidate")
        .first()
    )


def offer_list(project_id: int, candidate: CustomUser | None = None) -> QuerySet:
    queryset = Offer.objects.filter(project_id=project_id, is_cancelled=False)

    if candidate:
        queryset = queryset.filter(candidate=candidate)

    return queryset.all()
