from django.conf.urls import url

from . import views

urlpatterns = [
    url('^scribe/(?P<pk>\d+)/$', views.ScribeView.as_view(), name='scribe-sg'),
    url('^scribe/$', views.ScribeView.as_view(), name='scribe'),
    url('^$', views.MainView.as_view(), name='main'),
]
