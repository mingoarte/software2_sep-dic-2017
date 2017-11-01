from django.db import models
from django.utils import timezone
import datetime
from django import forms

class Faq(models.Model):
    fecha_creacion = models.DateTimeField('fecha de creacion:', null=True, default=timezone.now)

    def es_reciente(self):
        return self.fecha_publ >= timezone.now() - datetime.timedelta(days=1)

class Categoria(models.Model):
    faq = models.ForeignKey(Faq, on_delete=models.CASCADE, null=True)
    nombre = models.CharField('Tema:', max_length=100, blank=True)
    fecha_publ = models.DateTimeField('fecha de creacion:', null=True, default=timezone.now)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.nombre

class Pregunta(models.Model):
    faq = models.ForeignKey(Faq, on_delete=models.CASCADE, null=True)
    tema = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    pregunta = models.CharField('Pregunta:', max_length=100, blank=False, null=False)
    respuesta = models.TextField('Respuesta:', max_length=250, blank=False, null=False)

    class Meta:
            ordering = ["id"]

    def __str__(self):
        return self.pregunta
