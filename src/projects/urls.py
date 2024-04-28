from django.urls import path

from projects.views import (
    ProjectCreateView,
    ProjectDetailView,
    ProjectListView,
    ProjectMyListView,
)

app_name = "projects"
urlpatterns = [
    path("", ProjectListView.as_view(), name="list"),
    path("<int:pk>/", ProjectDetailView.as_view(), name="detail"),
    path("my/", ProjectMyListView.as_view(), name="my_list"),
    path("create/", ProjectCreateView.as_view(), name="create"),
]
