from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class buildTemplate(TemplateView):
    template_name = 'builder/build.html'

    def get_context_data(self, **kwargs):
        context = super(buildTemplate, self).get_context_data(**kwargs) 
        context['usuario'] = 'Kervyn'
       
        return context

    def post(request):
        return render(request, '/builder/build.html')

class homeTemplate(TemplateView):
	template_name = 'home.html'

class ver_templatesTemplate(TemplateView):
	template_name = 'ver_templates.html'
	