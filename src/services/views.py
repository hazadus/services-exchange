from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from exchange.selectors import category_get_by_id, category_list_only_available

from services.models import Service
from services.selectors import service_get_by_id, service_list


class ServiceListView(ListView):
    model = Service
    template_name = "services/service_list.html"

    def get_queryset(self):
        category_id = self.request.GET.get("category_id", None)
        return service_list(category_id=category_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        category_id = self.request.GET.get("category_id", None)

        if category_id is not None:
            category = category_get_by_id(category_id)
            context["category"] = category

        return context


class ServiceMyListView(LoginRequiredMixin, ListView):
    """Услуги залогиненного пользователя – страница "Мои услуги"."""

    model = Service
    template_name = "services/service_my_list.html"

    def get_queryset(self):
        return service_list(provider_id=self.request.user.id)


class ServiceDetailView(DetailView):
    model = Service
    template_name = "services/service_detail.html"

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)

        if pk is None:
            raise AttributeError(
                "Detail view %s must be called with an object "
                "pk in the URLconf." % self.__class__.__name__
            )

        return service_get_by_id(service_id=pk)


class ServiceCreateView(LoginRequiredMixin, CreateView):
    model = Service
    template_name = "services/service_create.html"
    fields = [
        "title",
        "category",
        "image",
        "description",
        "requirements",
        "price",
        "term",
        "portfolio_url",
    ]

    def get_form(self, form_class=None):
        """Оставляем в списке формы только категории, доступные для назначения услуге."""
        form = super().get_form(form_class)
        form.fields["category"].queryset = category_list_only_available()
        return form

    def form_valid(self, form):
        """Set logged in user as `provider` of new Service."""
        service = form.save(commit=False)
        service.provider = self.request.user
        service.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("services:detail", kwargs={"pk": self.object.pk})


class ServiceUpdateView(
    LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView
):
    model = Service
    fields = [
        "title",
        "category",
        "is_active",
        "image",
        "description",
        "requirements",
        "price",
        "term",
        "options",
        "portfolio_url",
    ]
    template_name = "services/service_update.html"
    success_message = "Сведения об услуге успешно изменены."

    def test_func(self):
        """Only allow user to update own service."""
        user = self.get_object().provider
        return user == self.request.user

    def get_success_url(self):
        return reverse_lazy("services:update", kwargs={"pk": self.get_object().pk})
