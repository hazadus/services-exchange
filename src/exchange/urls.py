from django.urls import path

from exchange.views import set_user_mode

app_name = "exchange"
urlpatterns = [
    path("/set_user_mode", set_user_mode, name="set_user_mode"),
]
