from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(("apps.router", "apps"), namespace="apps-api")),
    path("api/v1/auth/", include("djoser.urls")),
    path("api/v1/auth/", include("djoser.urls.jwt"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Fashion World Admin"
admin.site.site_title = "Drippers Admin Portal"
admin.site.index_title = "Welcome to the Standout Clique !!!"

