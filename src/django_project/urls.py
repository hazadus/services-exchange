from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path("accounts/", include("allauth.urls")),
        path("", include("core.urls")),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)


# Configure Admin panel titles
admin.site.site_header = "Биржа Услуг – Администрирование"
admin.site.site_title = "Биржа Услуг – Админка"
admin.site.index_title = "Биржа Услуг – Админка"
