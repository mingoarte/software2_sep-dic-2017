import json
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
from django.views.generic import TemplateView
from builder.models import *
from encuestas.models import *
from builder.forms import *
from encuestas.forms import *
from django.forms import formset_factory
from .forms import *
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.core import serializers
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.

class buildTemplate(TemplateView):
    template_name = 'builder/build.html'

    def get_context_data(self, **kwargs):
        context = super(buildTemplate, self).get_context_data(**kwargs)
              

        return context

    def post(self, request, *args, **kwargs):
        return render(request, '/builder/build.html')


class homeTemplate(TemplateView):
    template_name = 'home.html'

class ver_templatesTemplate(TemplateView):
    template_name = 'ver_templates.html'
    
    def get_context_data(self, **kwargs):
        context = super(ver_templatesTemplate, self).get_context_data(**kwargs) 
        context['templates'] = Template.objects.all()
        return context

class revisarTemplate(TemplateView):
    @staticmethod
    def get(request,templateID):

        template = Template.objects.get(id=templateID)
        print(template)
        return HttpResponse(template.html)


def pollConfig(request):
    
    question_text = request.GET.get('pregunta', None)
    options = request.GET.getlist('opciones[]', None)
    template_pk = request.GET.get('template', None)
    print(template_pk)
    template = Template.objects.get(pk=int(template_pk))

    question = Pregunta.objects.create(texto_pregunta=question_text,template=template)
    question_pk = question.pk
    question.save()

    question = Pregunta.objects.get(pk=question_pk)
    for option in options:
        Opcion.objects.create(pregunta=question, texto_opcion=option).save()
    # data = json.dumps(data, cls=DjangoJSONEncoder)
    # # json.simplejson.dumps(data)
    # data = serializers.serialize('json', preguntaForm)
    return JsonResponse(data={})


def newTemplate(request):
    name = request.GET.get('name', None)
    template = Template.objects.create(name=name)
    pk = template.pk
    template.save()
    return JsonResponse(data={'id': str(pk)})


