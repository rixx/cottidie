from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.shortcuts import redirect

from cottidie.diarium.models import Entry


class MainView(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    template_name = 'diarium/main.html'


class ScribeView(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    template_name = 'diarium/scribe.html'

    def post(self, request, pk=None):
        content = request.POST.get('entry')
        notebook = request.user.diaria.first()
        entry = Entry.objects.create(notebook=notebook, text=content)
        return redirect('diarium:scribe-sg', pk=entry.pk)
