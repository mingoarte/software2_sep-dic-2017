from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from .models import Carousel, Content

class CarouselForm(ModelForm):
    class Meta:
        model = Carousel
        fields = ['title', 'timer', 'auto', 'circular']
        labels = {
            'title': 'Título',
            'timer': 'Tiempo de transcición',
            'auto': 'Transición automática',
            'circular': 'Transcición circular'
        }

class ContentForm(ModelForm):
    class Meta:
        model = Content
        fields = ['title', 'description', 'image']
        labels = {
            'title': 'Título',
            'description': 'Descripción',
            'image': 'Imagen'
        }

CarouselFormSet = inlineformset_factory(Carousel, Content, form=ContentForm, fields='__all__', extra=1)
