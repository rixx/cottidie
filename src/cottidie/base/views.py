from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.utils.http import is_safe_url
from django.views.generic import TemplateView


class LoginView(TemplateView):
    template_name = 'base/login.html'

    def post(self, request):
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is None:
            return redirect('base:login')

        if not user.is_active:
            return redirect('base:login')

        login(request, user)
        url = request.GET.get('next')

        if url and is_safe_url(url, request.get_host()):
            return redirect(url)
        return redirect('base:main')


def logout_view(request):
    logout(request)
    return redirect('base:login')


class MainView(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    template_name = 'base/main.html'
