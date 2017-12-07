from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Formattedcontent
from builder.models import *
from .formatTranslator import *

@csrf_exempt
def formattedContentConfig(request):
	user = request.user
	title = request.POST.get('title', None)
	content = request.POST.get('content', None)
	template_pk = request.POST.get('template', None)
	position = request.POST.get('position', None)
	
	translator = FormatTranslator(content)
	translator.translateText()
	# En caso de que este modificando
	if position != None:
		template = Template.objects.get(pk=int(template_pk))
		component = TemplateComponent.objects.get(position=int(position), template=template)
		pattern = Formattedcontent.objects.get(template_component=component)
		pattern.title = title
		pattern.tagContent = content
		pattern.htmlContent = translator.translatedText
		pattern.save()
		
	# En caso de que este creando
	else:
		template = Template.objects.get(id=int(template_pk))
		patterns = template.sorted_patterns()

		if patterns:
			position = patterns[-1].template_component.get().position
			position += 1
		else:
			position = 0
		
		pattern = Formattedcontent.objects.create_pattern(title=title, tagContent=content, htmlContent = translator.translatedText, position=position, template=template)

	component = pattern.template_component.get()
		
	return JsonResponse(
        data={
        	'position' : position,
        	'html' : pattern.render_card()
        }
    )
	
def formattedContentDelete(request):
	pass
	
def formattedContentUpdate(request):
	pass
