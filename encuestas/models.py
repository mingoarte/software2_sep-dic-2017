from django.db import models
from django.utils import timezone
import datetime


class Pregunta(models.Model):
    texto_pregunta = models.CharField('Pregunta:', max_length=200)
    fecha_publ = models.DateTimeField('fecha de publicación', null=True, default=timezone.now)

    def es_reciente(self):
        return self.fecha_publ >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.texto_pregunta


class Opcion(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    texto_opcion = models.CharField('Opción:', max_length=200)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return self.texto_opcion
