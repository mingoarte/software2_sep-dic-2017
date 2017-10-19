from django import forms
from builder.models import *


class GenericForm(forms.ModelForm):
	class Meta:
		model = Generic
		exclude = ()

class AskForm(forms.ModelForm):
	class Meta:
		model = Pregunta
		fields = ('ask',)
