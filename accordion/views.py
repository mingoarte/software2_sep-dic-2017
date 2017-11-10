import json

from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.http import JsonResponse
from django.template.response import TemplateResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import AccordionForm
from .models import *


# View to create accordions
def accordionCreate(request):

    print("En el createeeeeeee niggaaaa")
    context = {}

    if request.method == 'POST':
        form = AccordionForm(request.POST)
        context['accordionForm'] = form

        if form.is_valid():
            panel_nro = form.cleaned_data['panels']
            parent = form.save()

            for i in range(0, panel_nro):
                Accordion(
                    title='Panel hijo',
                    parent=parent
                ).save()

            return HttpResponse(
                content=json.dumps({"redirectTo": reverse('accordion:accordion-list')}),
                content_type='application/json',
                status=200
            )

        # Error in form.
        return HttpResponse(json.dumps(form.errors), status=400)
    else:
        context['accordionForm'] = AccordionForm()

    return render(request, 'create_accordion.html', context)


# View to delete accordions
def accordionEdit(request, accordion_id):
    # Initialize context and search for accordion to edit
    try:
        accordion = Accordion.all_objects.get(accordion_id=accordion_id)
    except ObjectDoesNotExist:
        raise ObjectDoesNotExist()

    context = {
        'accordionForm': AccordionForm(),
        'accordion': accordion
    }

    if request.method == 'POST':
        form = AccordionForm(request.POST or None, instance=accordion)
        context['accordionFormEdit'] = form

        if form.is_valid():
            form.save()
    else:
        context['accordionFormEdit'] = AccordionForm(instance=accordion)

    return render(request, 'edit_accordion.html', context)


# View to delete accordions
def accordionDelete(request, accordion_id):
    # Get accordion to delete and delete it
    if request.method == 'GET':
        try:
            accordion = Accordion.all_objects.get(accordion_id=accordion_id)
        except ObjectDoesNotExist:
            raise ObjectDoesNotExist()
        accordion.delete()

    return redirect('accordion:accordion-list')
