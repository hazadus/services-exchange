import datetime

from django.contrib.contenttypes.models import ContentType
from django.utils import timezone

from users.models import Action


def action_create(user, verb: str, target=None) -> None:
    """
    Создает указанное действие, если не было аналогичных действий в течение 10 минут.
    Для 'verb' использовать константы из класса Action, например `Action.VIEW_PROJECT`.
    """
    # Выбираем аналогичные действия пользователя за последние десять минут
    now = timezone.now()
    last_ten_minutes = now - datetime.timedelta(seconds=600)
    similar_actions = Action.objects.filter(
        user_id=user.id, verb=verb, created__gte=last_ten_minutes
    )

    if target:
        target_ct = ContentType.objects.get_for_model(target)
        similar_actions = similar_actions.filter(
            target_ct=target_ct, target_id=target.id
        )

    if not similar_actions:
        Action.objects.create(user=user, verb=verb, target=target)
