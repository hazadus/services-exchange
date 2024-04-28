from django.urls import path

from projects.views import ProjectCreateView, ProjectMyListView

app_name = "projects"
urlpatterns = [
    path("my/", ProjectMyListView.as_view(), name="my_list"),
    path("create/", ProjectCreateView.as_view(), name="create"),
]
