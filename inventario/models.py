from select import select

from django.db import models
from django.forms import model_to_dict

from base.models import ClaseModelo


class TipoTransporte(ClaseModelo):
    nombre = models.CharField(
        max_length=60,
        help_text='Nombre del tipo de transporte',
        unique=True
    )

    def toJSON(self):
        item = model_to_dict(select)
        return item

    def _str_(self):
        return '{}'.format(self.nombre)

    def save(self):  # Guarda en mayuscula
        self.nombre = self.nombre.upper()
        super(TipoTransporte, self).save()

    class Meta:
        verbose_name_plural = 'TipoTransportes'
