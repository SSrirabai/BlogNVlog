# BlogNVlog/urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from blog.views import post_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', post_list, name='post_list'),
    # Add other paths as needed
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
