from django.views.generic import DetailView, ListView
from exchange.selectors import category_get_by_id

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
