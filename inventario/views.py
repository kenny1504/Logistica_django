from django.contrib.auth import login
from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin  # Mixin para authentication de usuario
from django.views import generic


class Home(LoginRequiredMixin, generic.TemplateView):

    template_name = 'braket/layout.html'
    login_url = '/login'  # si el usuario no esta autenticado envia a login
