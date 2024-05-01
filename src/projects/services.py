from users.models import CustomUser

from projects.models import Offer, Project


def offer_create(
    project: Project, candidate: CustomUser, comment: str | None = None
) -> Offer | None:
    """Создаёт предложение от кандидата на выполнение проекта, если от этого
    кандидата ещё нет предложений на данный проект."""
    if Offer.objects.filter(project=project, candidate=candidate).count():
        return None

    offer = Offer(project=project, candidate=candidate, comment=comment)
    offer.save()
    return offer


def offer_set_status(offer: Offer, new_status: str, actor: CustomUser) -> None:
    """Изменяет статус предложения на указанный (если это возможно)."""
    match new_status:
        case "cancelled":
            if (offer.status == "created") and (offer.candidate == actor):
                offer.status = "cancelled"
                offer.is_cancelled = True
        case "declined":
            if (offer.status == "created") and (offer.project.customer == actor):
                offer.status = "declined"
                offer.is_cancelled = True
        case _:
            return None
    offer.save()
