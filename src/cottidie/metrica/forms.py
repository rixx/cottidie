from django import forms

from cottidie.metrica.models import Goal, Measurement, Metric


class MetricForm(forms.ModelForm):

    class Meta:
        model = Metric
        exclude = []
        widgets = {
            'user': forms.widgets.HiddenInput,
        }
