from django.urls import path

from services.views import ServiceDetailView, ServiceListView

app_name = "services"
urlpatterns = [
    path("", ServiceListView.as_view(), name="list"),
    path("<int:pk>/", ServiceDetailView.as_view(), name="detail"),
]
