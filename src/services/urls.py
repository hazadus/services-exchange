from django.urls import path

from services.views import ServiceCreateView, ServiceDetailView, ServiceListView

app_name = "services"
urlpatterns = [
    path("", ServiceListView.as_view(), name="list"),
    path("<int:pk>/", ServiceDetailView.as_view(), name="detail"),
    path("create/", ServiceCreateView.as_view(), name="create"),
]
