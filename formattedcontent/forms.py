from django.forms import ModelForm
from .models import *

class FormattedContentForm(ModelForm):
	class Meta:
		model = FormattedContent
		fields = ['title']
		labels = { 'title' : 'Titulo' }
		
class ContentForm(ModelForm):
	class Meta:
		model = Content
		fields = ['text']
		labels = {
			'text' : 'Contenido'
		}
