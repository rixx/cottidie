from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.utils.timezone import now
from django.views.generic import FormView, TemplateView

from cottidie.metrica.forms import MeasurementForm, MetricForm
from cottidie.metrica.models import Measurement, Metric


class MainView(TemplateView):
    template_name = 'metrica/main.html'


class MetricDetailView(TemplateView):
    template_name = 'metrica/metric_detail.html'

    def get_context_data(self, pk: int) -> dict:
        ctx = super().get_context_data()
        qs = Metric.objects.filter(pk=pk, user=self.request.user)
        ctx['metric'] = qs.first() if qs.exists() else None
        return ctx


class MetricCreateView(FormView):
    form_class = MetricForm
    template_name = 'metrica/metric_create.html'

    def post(self, request):
        form = self.get_form()
        if form.is_valid():
            result = form.save()
            messages.success(request, 'You\'ve got a new metric!')
            return self.form_valid(form)
        else:
            messages.error(request, 'The metric could not be created.')
            return redirect('metrica:metric-create')

    def get_initial(self) -> dict:
        return {
            'user': self.request.user,
        }

    def get_success_url(self):
        return reverse('metrica:main')


class MeasurementCreateView(FormView):
    form_class = MeasurementForm
    template_name = 'metrica/measurement_create.html'

    def post(self, request, pk: int):
        form = self.get_form()
        if form.is_valid():
            result = form.save()
            messages.success(request, 'The measurement has been saved.')
            return self.form_valid(form)
        else:
            print(form.errors)
            messages.error(request, 'The metric could not be saved.')
            return redirect('metrica:measurement-create', pk=pk)

    def get_initial(self):
        return {
            'metric': Metric.objects.get(pk=self.kwargs['pk'])
        }

    def get_success_url(self):
        return reverse('metrica:main')
