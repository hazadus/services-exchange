from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("core.urls")),
]

# Configure Admin panel titles
admin.site.site_header = "Биржа Услуг – Администрирование"
admin.site.site_title = "Биржа Услуг – Админка"
admin.site.index_title = "Биржа Услуг – Админка"
