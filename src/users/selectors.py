from users.models import CustomUser


def get_user_by_username(username: str) -> CustomUser | None:
    return CustomUser.objects.filter(username=username).first()