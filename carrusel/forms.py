from django import forms
from .models import Carousel, Content

class CarouselForm(forms.ModelForm):
    class Meta:
        model = Carousel
        fields = ['title', 'count', 'timer', 'auto', 'circular']

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['title', 'description', 'image']
