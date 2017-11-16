import json
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from builder.models import *
from encuestas.models import *
from formBuilder.models import *
from captcha_pattern.models import *
from builder.forms import *
from encuestas.forms import *
from django.forms import formset_factory, model_to_dict
from .forms import *
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.core import serializers
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.loader import render_to_string


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
        context['captchaHTML'] = render_to_string('patrones/captcha/captcha.html', { 'public_key':'demoPublicKey' })
        #context['page_name'] = 'preview'
        return self.render_to_response(context)

@login_required(redirect_field_name='/')
@csrf_exempt
def formConfig(request):
    if request.method == 'POST':
        user = request.user
        form_json = json.loads(request.POST['form_json'])
        template_id = int(request.POST['template'])

        template = Template.objects.get(pk=template_id)
        patterns = template.sorted_patterns()
        position =  patterns[-1].position + 1 if len(patterns) else 0

        form = Formulario.objects.filter(template=template, position=position)
        if form.count():
            form.form_json = form_json
            form[0].save()
        else:
            form = Formulario.objects.create(form_json=form_json, template=template, position=position)
        return JsonResponse(form.form_json, safe=False)

@login_required(redirect_field_name='/')
@csrf_exempt
def captchaConfig(request):
    if request.method == 'POST':
        user = request.user

        # Extraemos las variables del form.
        template_id = int(request.POST.get('template', None))
        position = request.POST.get('position',None)
        public_key = request.POST.get('public_key', None)
        private_key = request.POST.get('private_key', None)

        print("{} - {}\n {}\n - {}".format(template_id, position, public_key, private_key))
        # Ya el template existe
        if position is not None and position != '':
            template = Template.objects.get(pk=template_id)
            component = TemplateComponent.objects.filter(position=int(position), template=template)
            captcha = Captcha.objects.filter(template_component=component)[0]
            captcha.public_key = public_key
            captcha.private_key = private_key
            captcha.save()

            return JsonResponse(data={'captcha': model_to_dict(captcha),
                                      'position': int(position),
                                      'nuevo_patron': False,})

        else:
            # Se obtiene el template ID junto con los patrones para poder
            # configurarle la posición a este patrón.
            template = Template.objects.get(pk=template_id)
            patterns = template.sorted_patterns()

            if patterns:
                position = patterns[-1].template_component.get().position
                position += 1
            else:
                position = 0

            captcha = Captcha.objects.create_pattern(public_key = public_key,
                                                     private_key = private_key,
                                                     position = position,
                                                     template = template)
            captcha.save()

            return JsonResponse(data={'captcha': model_to_dict(captcha),
                                      'position': captcha.template_component.get().position,
                                      'nuevo_patron': True,})

@login_required(redirect_field_name='/')
def eraseCaptcha(request):

    template_id = request.GET.get('template', None)
    position = request.GET.get('position', None)
    print(template_id,position)
    component = TemplateComponent.objects.filter(position=int(position), template_id=int(template_id))
    captcha = Captcha.objects.get(template_component=component)
    captcha.delete()
    return JsonResponse(data={})

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

        print(options)
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
