from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import FormView, TemplateView

from cottidie.occasiones.forms import OccasionTypeForm


class MainView(TemplateView):
    pass


class OccasionTypeView(TemplateView):
    pass


class OccasionTypeCreateView(FormView):
    form_class = OccasionTypeForm
    template_name = 'occasiones/occasion_type_create.html'

    def post(self, request):
        form = self.get_form()
        if form.is_valid():
            result = form.save()
            print(result)
            return self.form_valid(form)
        else:
            print(form.errors)
            return redirect('occasiones:occasion-type-create')

    def get_initial(self):
        return {
            'user': self.request.user,
        }

    def get_success_url(self):
        return reverse('occasiones:main')


class OccasionView(TemplateView):
    pass


class OccasionCreateView(TemplateView):
    pass
