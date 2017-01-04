from django.conf.urls import url

from . import views

urlpatterns = [
    url('^(?P<pk>\d+)/new/$', views.MeasurementCreateView.as_view(), name='measurement-create'),
    url('^(?P<pk>\d+)/$', views.MetricDetailView.as_view(), name='metric-detail'),
    url('^new/$', views.MetricCreateView.as_view(), name='metric-create'),
    url('^$', views.MainView.as_view(), name='main'),
]
