from django.urls import path

from services.views import ServiceListView

app_name = "services"
urlpatterns = [
    path("", ServiceListView.as_view(), name="list"),
]
