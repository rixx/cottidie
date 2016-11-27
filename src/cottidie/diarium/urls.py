from django.conf.urls import url

from . import views


urlpatterns = [
    url('^$', views.MainView.as_view(), name='main')
]
