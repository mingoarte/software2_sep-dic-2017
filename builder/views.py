from django.shortcuts import render
from django.views.generic import TemplateView
from builder.models import *
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.

class buildTemplate(TemplateView):
    template_name = 'builder/build.html'

    def get_context_data(self, **kwargs):
        context = super(buildTemplate, self).get_context_data(**kwargs)   
        return context

    def post(request):
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