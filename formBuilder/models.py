from django.db import models
from django.contrib.postgres.fields import JSONField
from builder.models import TemplateComponent

class Formulario(TemplateComponent):
    name = 'formulario'

    form_json = JSONField(default=dict)
