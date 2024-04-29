from django.contrib.contenttypes.models import ContentType
from django.db.models import QuerySet
from projects.models import Project
from services.models import Service

from users.models import Action, CustomUser


def user_get_by_username(username: str) -> CustomUser | None:
    return (
        CustomUser.objects.filter(username=username)
        .prefetch_related(
            "services", "services__category", "projects", "projects__category"
        )
        .first()
    )


def action_get_latest_service_views(user: CustomUser, count: int = 5) -> QuerySet:
    actions = Action.objects.filter(
        user=user,
        verb=Action.VIEW_SERVICE,
        target_ct=ContentType.objects.get_for_model(Service),
    )

    return actions[:count]


def action_get_latest_project_views(user: CustomUser, count: int = 5) -> QuerySet:
    actions = Action.objects.filter(
        user=user,
        verb=Action.VIEW_PROJECT,
        target_ct=ContentType.objects.get_for_model(Project),
    )

    return actions[:count]
