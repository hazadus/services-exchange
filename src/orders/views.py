from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import DetailView, ListView
from services.selectors import service_get_by_id
from users.selectors import action_list_for_order

from orders.forms import CreateServiceOrderForm
from orders.models import Order
from orders.selectors import order_list
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

        order = order_create(
            customer=request.user,
            provider=service.provider,
            item=service,
            price=service.price,
        )
        return redirect(reverse_lazy("orders:detail", kwargs={"pk": order.pk}))

    return redirect(reverse_lazy("services:list"))


class OrderDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Order
    template_name = "orders/order_detail.html"

    def test_func(self):
        """Только заказчик или исполнитель могут просматривать заказ"""
        order = self.get_object()
        return (order.customer == self.request.user) or (
            order.provider == self.request.user
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        order = self.get_object()
        actions = action_list_for_order(order_id=order.pk)
        context["actions"] = actions

        return context


class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = "orders/order_list.html"

    def get_queryset(self):
        return order_list(user_id=self.request.user.pk)
