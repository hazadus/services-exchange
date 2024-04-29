from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from services.selectors import service_get_by_id

from orders.forms import CreateServiceOrderForm
from orders.services import order_create


@require_POST
@login_required
def order_service_create_view(request: HttpRequest) -> HttpResponse:
    """Вид размещения заказа на услугу."""
    form = CreateServiceOrderForm(request.POST)

    if form.is_valid():
        data = form.cleaned_data
        service_id = data["service_id"]
        service = service_get_by_id(service_id=service_id)

        if not service:
            raise Http404

        order_create(
            customer=request.user,
            provider=service.provider,
            item=service,
            price=service.price,
        )

    return redirect(reverse_lazy("core:index"))
