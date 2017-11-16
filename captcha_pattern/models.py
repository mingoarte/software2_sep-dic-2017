from django.db import models
from django.contrib.postgres.fields import JSONField
from builder.models import Pattern

class Captcha(Pattern):
    name = 'captcha'

    def render(self):
	    return render_to_string('patrones/captcha_pattern/build.html', {"pattern": self})

    def __str__(self):
	    return "Captcha"
