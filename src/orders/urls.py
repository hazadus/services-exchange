from django.urls import path

from orders.views import OrderDetailView, OrderListView, order_service_create_view

app_name = "orders"
urlpatterns = [
    path("", OrderListView.as_view(), name="list"),
    path("<int:pk>/", OrderDetailView.as_view(), name="detail"),
    path("create/service/", order_service_create_view, name="create_service"),
]
