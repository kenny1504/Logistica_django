from logging import exception

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView

from inventario.models import TipoTransporte

""" index para mostrar vista de tipo de transporte"""


# Vista basada en clase
class TipoTransporteListView(ListView):
    model = TipoTransporte
    template_name = 'catalogos/tipoTransporte.html'

    @method_decorator(csrf_exempt)  # Decorador para omitir token
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'getdata':
                data = []
                for i in TipoTransporte.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)  # serializando objetos que no son diccionario
