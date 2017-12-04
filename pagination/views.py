import json
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template.loader import get_template
from builder.models import Template, TemplateComponent
from .forms import PaginationForm
from .models import Pagination
from django.views.decorators.csrf import csrf_exempt

def get_tempid_pos(request):
	#if request.method == 'GET':
	#	return request.GET.get("template", None), request.GET.get("position", None)
	#elif request.method == 'POST':
	return request.POST.get("template", None), request.POST.get("position", None)
		
def get_last_pos(template_id):
	template = Template.objects.get(pk = int(template_id))
	patterns = template.sorted_patterns()
	
	if patterns == []:
		position = 0
	else:
		position = patterns[-1].template_component.get().position
		position += 1
		
	return position

@csrf_exempt
def pagination_config(request):
	# Obtengo template_id y position de mi request
	title = request.POST.get('title', None)
	nItemsOnPage = request.POST.get('nItemsOnPage', None)
	content = request.POST.get('content', None)
	template_id = request.POST.get("template", None)
	template = Template.objects.get(pk=int(template_id))
	position = request.POST.get('position', None)
	
	# modificando
	if position != None:
		component = TemplateComponent.objects.get(position=int(position), template=template)
		pattern = Pagination.objects.get(template_component=component)
		pattern.title = title
		pattern.nItemsOnPage = nItemsOnPage
		pattern.content = content
		pattern.save()
	# creando
	else:
		position = get_last_pos(template_id)
		pattern = Pagination.objects.create_pattern(title=title, nItemsOnPage=nItemsOnPage, content=content, position=position, template=template)
		
	component = pattern.template_component.get()
	
	return JsonResponse(
		data={
			'position' : position,
			'html' : pattern.render_card()
		}
	)

def pagination_delete(request):
	pass

@csrf_exempt	
def pagination_update(request, pk):
	pass

