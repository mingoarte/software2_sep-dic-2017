import json
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
from django.views.generic import TemplateView
from builder.models import *
from encuestas.models import *
from carrusel.models import Carousel, Content
from builder.forms import *
from encuestas.forms import *
from carrusel.forms import *
from django.forms import formset_factory, model_to_dict
from .forms import *
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.core import serializers
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


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
    login_url = '/login/'
    redirect_field_name = '/'
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(**kwargs)
        prev = request.GET.get('type')
        print("KKKKKKKKKKKKKKKK")

        if prev is not None:
            context['page_name'] = prev
        else:
            context['page_name'] = 'revisar'

        template = Template.objects.get(id=(kwargs['templateID']))
        patterns = template.sorted_patterns()
        print(patterns)
        context['patterns'] = template.sorted_patterns()
        context['tem_id'] = kwargs['templateID']

        return self.render_to_response(context)

class editarTemplate(LoginRequiredMixin,TemplateView):
    login_url = '/login/'
    redirect_field_name = '/'
    template_name = 'builder/build.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        template = Template.objects.get(id=(kwargs['templateID']))
        patterns = template.sorted_patterns()
        components = TemplateComponent
        for pattern in patterns:
            print(pattern.template_component.get().position)
        context['patterns'] = patterns
        context['tem_id'] = kwargs['templateID']
        context['tem_name'] = template.name
        #context['page_name'] = 'preview'
        return self.render_to_response(context)


@login_required(redirect_field_name='/')
def pollConfig(request):
    user = request.user
    question_text = request.GET.get('pregunta', None)
    options = request.GET.getlist('opciones[]', None)
    template_pk = request.GET.get('template', None)
    position = request.GET.get('position', None)


    if position != '':
        template = Template.objects.get(pk=int(template_pk))
        component = TemplateComponent.objects.filter(position=int(position), template=template)
        question = Pregunta.objects.filter(template_component=component)
        question.texto_pregunta = question_text
        Opcion.objects.filter(pregunta=question).delete()

        for option in options:
            Opcion.objects.create(pregunta=question, texto_opcion=option).save()

        question.save()
        return JsonResponse(data={'question': model_to_dict(question), 
                            'options': list(options.values())})
    else:
        template = Template.objects.get(id=int(template_pk))
        patterns = template.sorted_patterns()

        if patterns:
            position = patterns[-1].template_component.get().position
            position += 1
        else:
            position = 0

        question = Pregunta.objects.create_pattern(texto_pregunta=question_text, position=position, template=template)
        question.save()

        for option in options:
            Opcion.objects.create(pregunta=question, texto_opcion=option).save()
        options = Opcion.objects.filter(pregunta=question).order_by('id')

        return JsonResponse(data={'question': model_to_dict(question), 
                            'options': list(options.values()),
                            'position': question.template_component.get().position})


    # print (options)
    # p1 = list(question.values('texto_pregunta', 'template', 'position'))
    # p2 = list(options.values())


@login_required(redirect_field_name='/')
def carouselConfig(request):
    user = request.user
    carousel = {
        'title': request.GET.get('title', None),
        'count': request.GET.get('count', None),
        'timer': request.GET.get('timer', None),
        'auto': request.GET.get('auto', None).capitalize(),
        'circular': request.GET.get('circular', None).capitalize(),
        'descriptions': request.GET.getlist('descriptions[]', None),
        'images': request.GET.getlist('images[]', None),
    }
    #print(carousel)
    template_pk = request.GET.get('template', None)
    position = request.GET.get('position', '0')
    created = request.GET.get('created', None)

    template = Template.objects.get(pk=int(template_pk))
    obj = Carousel.objects.filter(template=template, position=int(position))
    if obj.count():
        obj[0].title = carousel['title']
        obj[0].timer = carousel['timer']
        obj[0].auto = carousel['auto']
        obj[0].circular = carousel['circular']
        '''options2 = Opcion.objects.filter(pregunta=question[0]).delete()

        print(options)
        for option in options:
            Opcion.objects.create(pregunta=question[0], texto_opcion=option).save()
        '''
        obj[0].save()
    else:
        obj = Carousel.objects.create(title=carousel['title'], count=carousel['count'], 
            timer=carousel['timer'], auto=carousel['auto'], circular=carousel['circular'], 
            template=template, position=int(position))
        obj_pk = obj.pk
        #print("Primary Key: ", obj_pk)
        obj.save()
        obj = Carousel.objects.filter(pk=obj_pk)

        for index, elem in enumerate(carousel['descriptions']):
            #print("Description: ", elem)
            #print("Image: ", carousel['images'][index])
            obj_content = Content.objects.create(carousel=obj[0], description=elem, 
              image=carousel['images'][index], title=elem)
            obj_content.save()
    
    contents = Content.objects.filter(carousel=obj)
    p1 = list(obj.values('title', 'count', 'timer', 'circular', 'template', 'position'))
    p2 = list(contents.values('description', 'image'))
    return JsonResponse(data={'carousel': p1, 'contents': p2})


@login_required(redirect_field_name='/')
def newTemplate(request):
    name = request.GET.get('name', None)
    template = Template.objects.create(name=name)
    pk = template.pk
    template.save()
    return JsonResponse(data={'id': str(pk)})


@login_required(redirect_field_name='/')
def eraseQuestion(request):

    template_id = request.GET.get('template', None)
    position = request.GET.get('position', None)
    print(template_id,position)
    component = TemplateComponent.objects.filter(position=int(position), template_id=int(template_id))
    question = Pregunta.objects.get(template_component=component)
    question.delete()
    return JsonResponse(data={})

@login_required(redirect_field_name='/')
def createPoll(request):
    template_id = request.GET.get('template', None)
    template = Template.objects.get(id=int(template_id))
    patterns = template.sorted_patterns()

    if patterns:
        position = patterns.last().get().position
        position += 1
    else:
        position = 0
    
    return JsonResponse(data={'position':position,})

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
