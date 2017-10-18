from __future__ import unicode_literals

from django.db import models
import random
from .utils import random_string

class KeyPair(models.Model):
    public_key = models.CharField(primary_key=True, max_length=64, default=random_string.alphanumeric)
    private_key = models.CharField(max_length=64, default=random_string.alphanumeric, unique=True)

class GeneratedCaptcha(models.Model):
    captcha_id = models.CharField(max_length=64, unique=True, default=random_string.alphanumeric)
    keypair = models.ForeignKey(KeyPair)
    answer = models.CharField(max_length=30)
