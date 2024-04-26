from django.urls import path

from users.views import PublicUserProfileView, UpdateUserView

app_name = "users"
urlpatterns = [
    path("update/<int:pk>/", UpdateUserView.as_view(), name="update"),
    path("<str:username>/", PublicUserProfileView.as_view(), name="public_profile"),
]
