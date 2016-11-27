from django.conf.urls import url

from . import views


urlpatterns = [
    url('^scribe/', views.ScribeView.as_view(), name='scribe'),
    url('^$', views.MainView.as_view(), name='main'),
]
