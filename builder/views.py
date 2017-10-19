from django.shortcuts import render
from django.views.generic import TemplateView
from builder.models import *
from builder.forms import *

# Create your views here.

class buildTemplate(TemplateView):
    template_name = 'builder/build.html'

    def get_context_data(self, **kwargs):
        context = super(buildTemplate, self).get_context_data(**kwargs)
        context['generic'] = GenericForm()
        context['generic2'] = GenericForm()
        context['pregunta'] = AskForm()        
        context['pregunta2'] = AskForm()        

        return context

    def post(self, request, *args, **kwargs):
    	return render(request, '/builder/build.html')

def pollConfig(request):
    print("ENTRO")
    # amount = request.GET.get('amount', None)
    # product_name = request.GET.get('name', None)
    # unit_name = request.GET.get('unit', None)
    # product = Product.objects.get(name=product_name)
    # unit = UnitTable.objects.get(name=unit_name)
    # convertRelation = ConversionTable.objects.get(product_id=product.pk, unit_id=unit.pk)
    # data = {
    #     'total': round(Decimal(amount) * product.selling_price * convertRelation.relation, 2),
    #     'id': product.id,
    #     'price': Decimal(round(product.selling_price * convertRelation.relation, 2)),
    #     'unit': unit_name
    # }
    # return JsonResponse(data)