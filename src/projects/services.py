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
