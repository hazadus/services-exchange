from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView

from users.models import CustomUser
from users.selectors import (
    action_get_latest_project_views,
    action_get_latest_service_views,
    user_get_by_username,
)


class PublicUserProfileView(TemplateView):
    template_name = "users/user_public_profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        username = context.get("username", None)
        if username is None:
            raise Http404

        public_user = user_get_by_username(username)
        if public_user is None:
            raise Http404

        context["public_user"] = public_user

        if self.request.user == public_user:
            # Если пользователь смотрит свой публичный профиль, добаим инфо
            # о последних просмотренных услугах и проектах
            context["actions_services_viewed"] = action_get_latest_service_views(
                user=public_user
            )
            context["actions_projects_viewed"] = action_get_latest_project_views(
                user=public_user
            )

        return context


class UpdateUserView(
    LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView
):
    model = CustomUser
    fields = [
        "username",
        "first_name",
        "last_name",
        "profile_image",
        "speciality",
        "description",
        "skills",
        "country",
        "city",
        "phone",
    ]
    template_name = "users/user_update.html"
    success_message = "Информация пользователя успешно изменена!"

    def test_func(self):
        """Only allow user to update own profile."""
        user = self.get_object()
        return user == self.request.user

    def get_success_url(self):
        return reverse_lazy("users:update", kwargs={"pk": self.get_object().pk})
