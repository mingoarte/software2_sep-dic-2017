from django.db import models
from builder.models import TemplateComponent

class Carousel(TemplateComponent):
    title = models.CharField(max_length=50)
    timer = models.IntegerField(blank=True, default=3)
    auto = models.BooleanField(default=False)
    circular = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Content(models.Model):
    carousel = models.ForeignKey(Carousel, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=256, blank=True)
    image = models.ImageField(upload_to='carouselImages/', blank=True)

    def __str__(self):
        return self.title
