from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.template.defaultfilters import default


# Clase general del sistema
class ClaseModelo(models.Model):
    estado = models.IntegerField(default=1)
    fecha_guardado = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, null=True)
    usuario_grabacion = models.ForeignKey(User, on_delete=models.CASCADE)
    usuario_modifica = models.IntegerField(blank=True, null=True)

    class Meta:
        abstract = True

