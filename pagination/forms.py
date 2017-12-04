#from django.forms import ModelForm, widgets, Form
from django import forms
import django.apps

aux = django.apps.apps.get_models()
cont_choices = []
for elem in aux:
	if(hasattr(elem, 'name') and type(elem.name) == str):
		cont_choices.append((elem.name, elem.name))

class PaginationForm(forms.Form):
	title = forms.CharField(max_length=50)
	nItemsOnPage = forms.IntegerField(initial = 5)
	content = forms.ChoiceField(choices = cont_choices)
	choices = cont_choices
