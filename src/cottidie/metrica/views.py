from django.views.generic import FormView, TemplateView


class MainView(TemplateView):
    template_name = 'metrica/main.html'
