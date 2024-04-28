from django.urls import path

from projects.views import (
    ProjectCreateView,
    ProjectDeleteView,
    ProjectDetailView,
    ProjectListView,
    ProjectMyListView,
    ProjectUpdateView,
)

app_name = "projects"
urlpatterns = [
    path("", ProjectListView.as_view(), name="list"),
    path("<int:pk>/", ProjectDetailView.as_view(), name="detail"),
    path("my/", ProjectMyListView.as_view(), name="my_list"),
    path("create/", ProjectCreateView.as_view(), name="create"),
    path("update/<int:pk>/", ProjectUpdateView.as_view(), name="update"),
    path("delete/<int:pk>/", ProjectDeleteView.as_view(), name="delete"),
]
