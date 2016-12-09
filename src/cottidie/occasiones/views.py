from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.utils.timezone import now
from django.views.generic import FormView, TemplateView

from cottidie.occasiones.forms import OccasionForm, OccasionTypeForm
from cottidie.occasiones.models import OccasionType


class MainView(TemplateView):
    template_name = 'occasiones/main.html'


class OccasionTypeView(TemplateView):
    template_name = 'occasiones/occasion_list.html'

    def get_context_data(self, pk: int) -> dict:
        ctx = super().get_context_data()
        qs = OccasionType.objects.filter(pk=pk, user=self.request.user)
        ctx['occasion_type'] = qs.first() if qs.exists() else None
        return ctx


class OccasionTypeCreateView(FormView):
    form_class = OccasionTypeForm
    template_name = 'occasiones/occasion_type_create.html'

    def post(self, request):
        form = self.get_form()
        if form.is_valid():
            result = form.save()
            return self.form_valid(form)
        else:
            return redirect('occasiones:occasion-type-create')

    def get_initial(self) -> dict:
        return {
            'user': self.request.user,
        }

    def get_success_url(self):
        return reverse('occasiones:main')


class OccasionCreateView(FormView):
    form_class = OccasionForm
    template_name = 'occasiones/occasion_create.html'

    def post(self, request, pk: int):
        form = self.get_form()
        if form.is_valid():
            result = form.save()
            return self.form_valid(form)
        else:
            print(form.errors)
            return redirect('occasiones:occasion-create', pk=pk)

    def get_initial(self) -> dict:
        return {
            'typus': OccasionType.objects.filter(
                user=self.request.user,
                pk=self.kwargs['pk'],
            ).first(),
            'end': now(),
        }

    def get_success_url(self):
        return reverse('occasiones:main')
