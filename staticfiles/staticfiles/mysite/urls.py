from django.contrib import admin
from django.urls import path, include
#^ import
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('console/', admin.site.urls),
    path('', include("data.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
