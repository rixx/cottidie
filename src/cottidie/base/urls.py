from django.conf.urls import url

from . import views


urlpatterns = [
    url('^login/$', views.LoginView.as_view(), name='login'),
    url('^logout/$', views.logout_view, name='logout'),
    url('^$', views.MainView.as_view(), name='main'),
]
