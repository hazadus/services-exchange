from django.urls import path

from exchange.views import CategoryListView, set_user_mode

app_name = "exchange"
urlpatterns = [
    path("set_user_mode/", set_user_mode, name="set_user_mode"),
    path("categories/", CategoryListView.as_view(), name="category_list"),
]
