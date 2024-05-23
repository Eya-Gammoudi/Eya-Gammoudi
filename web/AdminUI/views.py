from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from .decorators import superuser_required

class AdminLoginView(LoginView):
    template_name = 'admin/login.html'
    redirect_authenticated_user = True


class AdminLogoutView(LogoutView):
    next_page = reverse_lazy('adminUI:login')


@login_required
@superuser_required
def adminUI(request):
    context = {}
    return render(request, 'adminUI.html', context)


def google_maps(request):
    context = {
        'parent': 'maps',
        'segment': 'google_maps'
    }
    return render(request, 'pages/map-google.html', context)
