from django import forms

from cottidie.occasiones.models import OccasionType


class OccasionTypeForm(forms.ModelForm):

    class Meta:
        model = OccasionType
        exclude = []
        widgets = {
            'user': forms.widgets.HiddenInput,
        }


class OccasionForm(forms.Form):
    pass
