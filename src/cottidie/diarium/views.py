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
        words = request.POST.get('words')
        characters = request.POST.get('characters')

        if pk:
            qs = Entry.objects.filter(
                notebook__user=self.request.user,
                pk=pk,
            )
            if qs.exists():  # TODO: find out how many words were added, save that information
                entry = qs.first()
                entry.text = content
                entry.word_count = words
                entry.character_count = characters
                entry.save(update_fields=['text', 'word_count', 'character_count'])
        else:
            notebook = request.user.diarium.default
            entry = Entry.objects.create(
                notebook=notebook,
                text=content,
                word_count=words,
                character_count=characters,
            )
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
