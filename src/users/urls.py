from django.urls import path

from users.views import (
    UserPublicProfileView,
    UserUpdateBalanceView,
    UserUpdateProfileView,
)

app_name = "users"
urlpatterns = [
    path("update/<int:pk>/", UserUpdateProfileView.as_view(), name="update"),
    path("balance/", UserUpdateBalanceView.as_view(), name="update_balance"),
    path("<str:username>/", UserPublicProfileView.as_view(), name="public_profile"),
]
