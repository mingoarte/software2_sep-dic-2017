from django.db import models
from builder.models import Pattern, TemplateComponent
from django.template.loader import render_to_string
from django.template import RequestContext
from django.shortcuts import render

class Formattedcontent(Pattern):
	name = 'formattedContent'
	title = models.CharField(max_length = 100)
	tagContent = models.CharField(max_length = 3000, default='')
	htmlContent = models.CharField(max_length = 5000, default='')
	
	# Pattern's html
	def render(self):
		return render_to_string('patrones/formattedContent/view.html', {"pattern": self})
	
	# Config modal html
	def render_config_modal(self, request):
		context = {
			'pattern' : self
		}
		return render_to_string('patrones/formattedContent/configurar-modal.html', context)
	
	# Constructor card html
	def render_card(self):
		return render_to_string('patrones/formattedContent/build.html', {"pattern": self})
		
	def __str__(self):
		return 'Fomatted Content N'+str(self.pk)
		
		
