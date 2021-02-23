from django.urls import path

from inventario.views import  Home

urlpatterns = [

    path('', Home.as_view(), name='home'),

]
