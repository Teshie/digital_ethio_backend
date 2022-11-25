from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
urlpatterns = [
	 path("admin/", admin.site.urls),
	 path("api/account/", include("accounts.urls")),
	 path("api/department/", include("department.urls")),
]


if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = settings.ADMIN_SITE_HEADER
