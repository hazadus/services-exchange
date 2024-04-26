from django.urls import path

from users.views import UserProfileView

app_name = "users"
urlpatterns = [
    path("update/<int:pk>/", UserProfileView.as_view(), name="update"),
]
