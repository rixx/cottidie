from django import forms

from cottidie.metrica.models import Goal, Measurement, Metric


class MetricForm(forms.ModelForm):

    class Meta:
        model = Metric
        exclude = []
        widgets = {
            'user': forms.widgets.HiddenInput,
        }


class MeasurementForm(forms.ModelForm):

    class Meta:
        model = Measurement
        exclude = []
        widgets = {
            'note': forms.widgets.Textarea,  # will be adjusted accordin to metric type
            'metric': forms.widgets.HiddenInput,
        }


class Goal(forms.ModelForm):

    class Meta:
        model = Goal
        exclude = []
        widgets = {
            'motivation_text': forms.widgets.Textarea,
            'metric': forms.widgets.HiddenInput,
        }
