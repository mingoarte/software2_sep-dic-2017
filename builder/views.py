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
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class buildTemplate(LoginRequiredMixin,TemplateView):
    login_url = '/login/'
    redirect_field_name = '/'
    template_name = 'builder/build.html'

    def get_context_data(self, **kwargs):
        context = super(buildTemplate, self).get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
    	return render(request, '/builder/build.html')



class homeTemplate(TemplateView):
    template_name = 'home.html'

class ver_templatesTemplate(LoginRequiredMixin,TemplateView):
    login_url = '/login/'
    redirect_field_name = '/'
    template_name = 'ver_templates.html'
    
    def get_context_data(self, **kwargs):
        context = super(ver_templatesTemplate, self).get_context_data(**kwargs)

        context['templates'] = Template.objects.all()
        return context

class revisarTemplate(LoginRequiredMixin,TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(**kwargs)
        
        template = Template.objects.get(id=(kwargs['templateID']))
        questions = Pregunta.objects.filter(template=template).order_by('position')
        patterns = []
        for question in questions:
            pattern = {'question': question,
                        'options': Opcion.objects.filter(pregunta=question)}
            patterns.append(pattern)
        context['patterns'] = patterns
        return self.render_to_response(context)

@login_required(redirect_field_name='/')
def pollConfig(request):
    user = request.user
    question_text = request.GET.get('pregunta', None)
    options = request.GET.getlist('opciones[]', None)
    template_pk = request.GET.get('template', None)
    position = request.GET.get('position', None)
    guardado = request.GET.get('guardado', None)

    
    template = Template.objects.get(pk=int(template_pk))
    print('')
    print(guardado)
    if request.GET.get('pregunta_pk')!='':
        print("entre if")
        question_pk = request.GET.get('pregunta_pk', None)
        question = Pregunta.objects.filter(pk=question_pk)
        question.update(texto_pregunta=question_text)
        for option in options:
            option.update(pregunta=question, texto_opcion=option)

    else:
        print("entre else")

        question = Pregunta.objects.create(texto_pregunta=question_text,template=template,position=int(position))
        question_pk = question.pk
        question.save()

        question = Pregunta.objects.get(pk=question_pk)
        for option in options:
            Opcion.objects.create(pregunta=question, texto_opcion=option).save()
        # data = json.dumps(data, cls=DjangoJSONEncoder)
        # # json.simplejson.dumps(data)
        # data = serializers.serialize('json', preguntaForm)
    return JsonResponse(data={'pregunta_pk':question})

@login_required(redirect_field_name='/')
def newTemplate(request):
    name = request.GET.get('name', None)
    template = Template.objects.create(name=name)
    pk = template.pk
    template.save()
    return JsonResponse(data={'id': str(pk)})

class userTemplate(TemplateView):
    template_name = 'crear_usuario.html'

    def get_context_data(self, **kwargs):
        context = super(userTemplate, self).get_context_data(**kwargs)
        context['form'] = registerForm()
        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = registerForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')

        else:
            form = registerForm()

        return render(request, 'crear_usuario.html',{'form': form})

class loginTemplate(TemplateView):
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        context = super(loginTemplate, self).get_context_data(**kwargs)
        context['form'] = loginForm()
        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = loginForm(request.POST)
            if form.is_valid():
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(username=username,password=password)

                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/')

        else:
            form = registerForm()

        return render(request, 'login.html',{'form': form}) 

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")

