from __future__ import unicode_literals

from django.db import models
from .utils import random_string

class GeneratedCaptcha(models.Model):
    id = models.AutoField(primary_key=True, default=random_string.alphanumeric)
    client_key = models.CharField(max_length=64)
    answer = models.CharField(max_length=30)
    valid = models.BooleanField(default=True)
