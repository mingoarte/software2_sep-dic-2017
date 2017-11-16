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
from django.forms import formset_factory
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

        # TODO: Refactorizar: DRY
        patterns = template.sorted_patterns()
        for pattern in patterns:
            if pattern.name == 'formulario':
                pattern.form_json = json.dumps(pattern.form_json)
        context['patterns'] = patterns

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
        for pattern in patterns:
            if pattern.name == 'formulario':
                pattern.form_json = json.dumps(pattern.form_json)
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
        template_id = int(request.POST['template'])
        template = Template.objects.get(pk=template_id)
        patterns = template.sorted_patterns()
        position =  patterns[-1].position + 1 if len(patterns) else 0

        captcha = Captcha.objects.filter(template=template, position=position)
        print(template_id, position)
        if captcha.count():
            captcha[0].save()
        else:
            captcha = Captcha.objects.create(template=template, position=position)
        return JsonResponse({}, safe=False)

@login_required(redirect_field_name='/')
def pollConfig(request):
    user = request.user
    question_text = request.GET.get('pregunta', None)
    options = request.GET.getlist('opciones[]', None)
    template_pk = request.GET.get('template', None)
    position = request.GET.get('position', None)
    created = request.GET.get('created', None)

    print ("\n\n\n")
    print (position)

    template = Template.objects.get(pk=int(template_pk))
    question = Pregunta.objects.filter(template=template, position=int(position))
    print (question_text)
    print ("\n\n\n")
    if question.count():
        print("ENTRO")
        question[0].texto_pregunta = question_text
        options2 = Opcion.objects.filter(pregunta=question[0]).delete()
        print(options2)
        # options2 = question[0].opcion_set.all()
        # print(options2)
        # for option in options2:
        #     option.delete()

        print(options)
        for option in options:
            Opcion.objects.create(pregunta=question[0], texto_opcion=option).save()

        question[0].save()
    else:
        question = Pregunta.objects.create(texto_pregunta=question_text,template=template,position=int(position))
        question_pk = question.pk
        question.save()

        question = Pregunta.objects.filter(pk=question_pk)
        for option in options:
            Opcion.objects.create(pregunta=question[0], texto_opcion=option).save()

    options = Opcion.objects.filter(pregunta=question)
    # print (options)
    p1 = list(question.values('texto_pregunta', 'template', 'position'))
    p2 = list(options.values())

    return JsonResponse(data={'question': p1, 'options': p2})

@login_required(redirect_field_name='/')
def newTemplate(request):
    name = request.GET.get('name', None)
    template = Template.objects.create(name=name)
    pk = template.pk
    template.save()
    return JsonResponse(data={'id': str(pk)})


@login_required(redirect_field_name='/')
def eraseFormulario(request):

    template_id = request.GET.get('template', None)
    position = request.GET.get('position', None)
    template = Template.objects.get(id=int(template_id))
    form = Formulario.objects.get(template=template, position=int(position))
    form.delete()
    return JsonResponse(data={})

@login_required(redirect_field_name='/')
def eraseQuestion(request):

    template_id = request.GET.get('template', None)
    position = request.GET.get('position', None)
    template = Template.objects.get(id=int(template_id))
    question = Pregunta.objects.get(template=template, position=int(position))
    question.delete()
    return JsonResponse(data={})

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
