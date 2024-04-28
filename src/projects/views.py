from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from exchange.selectors import category_list_only_available

from projects.models import Project
from projects.selectors import project_list


class ProjectMyListView(LoginRequiredMixin, ListView):
    """Проекты залогиненного пользователя – страница "Мои проекты"."""

    model = Project
    template_name = "projects/project_my_list.html"

    def get_queryset(self):
        return project_list(customer_id=self.request.user.id)


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = "projects/project_create.html"
    fields = [
        "title",
        "category",
        "description",
        "price",
        "is_higher_price_allowed",
        "max_price",
    ]

    def get_form(self, form_class=None):
        """Оставляем в списке формы только категории, доступные для назначения услуге."""
        form = super().get_form(form_class)
        form.fields["category"].queryset = category_list_only_available()
        return form

    def form_valid(self, form):
        """Set logged in user as `customer` of new Project."""
        service = form.save(commit=False)
        service.customer = self.request.user
        service.save()
        return super().form_valid(form)

    # def get_success_url(self):
    #     return reverse_lazy("projects:detail", kwargs={"pk": self.object.pk})
