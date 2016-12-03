from django import forms

from cottidie.occasiones.models import Occasion, OccasionType


class OccasionTypeForm(forms.ModelForm):

    class Meta:
        model = OccasionType
        exclude = []
        widgets = {
            'user': forms.widgets.HiddenInput,
        }


class OccasionForm(forms.ModelForm):

    class Meta:
        model = Occasion
        exclude = []
        widgets = {
            'note': forms.widgets.Textarea,
            'typus': forms.widgets.HiddenInput,
        }
