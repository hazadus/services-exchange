from django.urls import path

from orders.views import order_service_create_view

app_name = "orders"
urlpatterns = [
    path("create/service/", order_service_create_view, name="create_service"),
]
