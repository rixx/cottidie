from django.conf.urls import include, url
from django.contrib import admin

from .base import urls as baseurls
from .diarium import urls as diariumurls
from .metrica import urls as metricaurls
from .occasiones import urls as occasionesurls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^diarium/', include(diariumurls, namespace='diarium')),
    url(r'^metrica/', include(metricaurls, namespace='metrica')),
    url(r'^occasiones/', include(occasionesurls, namespace='occasiones')),
    url(r'', include(baseurls, namespace='base')),
]
