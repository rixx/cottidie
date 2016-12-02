from django.conf.urls import url

from . import views


urlpatterns = [
    url('^occasio/(?P<pk>\d+)/new/$', views.OccasionCreateView.as_view(), name='occasion-create'),
    url('^occasio/(?P<pk>\d+)/$', views.OccasionView.as_view(), name='occasion-type'),
    url('^occasio/new/$', views.OccasionTypeCreateView.as_view(), name='occasions-type-create'),
    url('^occasio/$', views.OccasionTypeView.as_view(), name='occasions-type-list'),
    url('^$', views.MainView.as_view(), name='main'),
]
