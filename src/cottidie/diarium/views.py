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

    def get_context_data(self, pk=None):
        ctx = super().get_context_data()

        if pk:
            qs = Entry.objects.filter(
                notebook__user=self.request.user,
                pk=pk,
            )
            if qs.exists():
                ctx['entry_data'] = qs.first().text

        return ctx

    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            qs = Entry.objects.filter(
                notebook__user=self.request.user,
                pk=pk,
            )
            if not qs.exists():
                return redirect('diarium:scribe')
        return super().get(self, *args, **kwargs)
