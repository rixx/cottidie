from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.utils.timezone import now
from django.views.generic import FormView, TemplateView

from cottidie.metrica.forms import MeasurementForm, MetricForm
from cottidie.metrica.models import Measurement, Metric


class MainView(TemplateView):
    template_name = 'metrica/main.html'


class MetricCreateView(FormView):
    form_class = MetricForm
    template_name = 'metrica/metric_create.html'

    def post(self, request):
        form = self.get_form()
        if form.is_valid():
            result = form.save()
            return self.form_valid(form)
        else:
            return redirect('metrica:metric-create')

    def get_initial(self) -> dict:
        return {
            'user': self.request.user,
        }

    def get_success_url(self):
        return reverse('metrica:main')
