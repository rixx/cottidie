from django.conf.urls import include, url
from django.contrib import admin

from .base import urls as baseurls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include(baseurls, namespace='base')),
]
