from django.urls import path

from services.views import (
    ServiceCreateView,
    ServiceDetailView,
    ServiceListView,
    ServiceMyListView,
)

app_name = "services"
urlpatterns = [
    path("", ServiceListView.as_view(), name="list"),
    path("my/", ServiceMyListView.as_view(), name="my_list"),
    path("<int:pk>/", ServiceDetailView.as_view(), name="detail"),
    path("create/", ServiceCreateView.as_view(), name="create"),
]
