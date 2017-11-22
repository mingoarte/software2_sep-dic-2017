from django.db import models
from django.core.validators import MinValueValidator
from builder.models import Pattern
from django.template.loader import render_to_string

class Carousel(Pattern):
    name = 'Carrusel'
    title = models.CharField(max_length=50)
    timer = models.IntegerField(blank=True, default=3, validators=[MinValueValidator(0)])
    auto = models.BooleanField(default=False)
    circular = models.BooleanField(default=True)

    def render(self):
        return render_to_string('patrones/carrusel/build.html', {"pattern": self})

    def __str__(self):
        return self.name + ": " + str(self.pk) + "; title:" + self.title + "; timer: " + str(self.timer)

class Content(models.Model):
    carousel = models.ForeignKey(Carousel, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=256, blank=True)
    image = models.ImageField(upload_to='carouselImages/')

    def __str__(self):
        return self.title
