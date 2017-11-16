from django.db import models
from django.contrib.postgres.fields import JSONField
from builder.models import TemplateComponent

class Captcha(TemplateComponent):
    name = 'captcha'
