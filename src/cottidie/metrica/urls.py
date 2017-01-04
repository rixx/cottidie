from django.conf.urls import url

from . import views

urlpatterns = [
    url('^new/$', views.MetricCreateView.as_view(), name='metric-create'),
    url('^$', views.MainView.as_view(), name='main'),
]
