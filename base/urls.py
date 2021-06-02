from django.urls import path
# Vistas por defect para login y logout
from django.contrib.auth import views as auth_views

from base.views import Home

urlpatterns = [

    path('', Home.as_view(), name='home'),
    # Ruta para login
    path('login/', auth_views.LoginView.as_view(template_name='login/login.html'), name='login'),
    # Ruta para logout
    path('logout/', auth_views.LogoutView.as_view(template_name='login/login.html'), name='logout')

]
