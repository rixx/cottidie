from django.conf.urls import include, url
from django.contrib import admin

from .base import urls as baseurls
from .diarium import urls as diariumurls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^diarium/', include(diariumurls, namespace='diarium')),
    url(r'', include(baseurls, namespace='base')),
]
