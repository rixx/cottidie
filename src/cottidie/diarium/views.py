from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class MainView(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    template_name = 'diarium/main.html'


class ScribeView(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    template_name = 'diarium/scribe.html'
