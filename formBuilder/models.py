from django.db import models
from django.contrib.postgres.fields import JSONField
from builder.models import Pattern

class Formulario(Pattern):
    name = 'formulario'

    form_json = JSONField(default=dict)
