from django.views.generic import ListView
from exchange.selectors import category_get_by_id

from services.models import Service
from services.selectors import service_list


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
