from django.conf.urls import url

from . import views


urlpatterns = [
    url('^(?P<pk>\d+)/new/$', views.OccasionCreateView.as_view(), name='occasion-create'),
    url('^(?P<pk>\d+)/$', views.OccasionView.as_view(), name='occasion-type'),
    url('^list/$', views.OccasionTypeView.as_view(), name='occasion-type-list'),
    url('^new/$', views.OccasionTypeCreateView.as_view(), name='occasion-type-create'),
    url('^$', views.MainView.as_view(), name='main'),
]
