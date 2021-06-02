from django.urls import path

from inventario.views import *

urlpatterns = [

    path('tipoTransporte/', TipoTransporteListView.as_view(), name='tipoTransporte'),  # URL de aplicacion

]
