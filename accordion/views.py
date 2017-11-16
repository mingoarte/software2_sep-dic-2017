import json

from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.http import JsonResponse
from django.template.response import TemplateResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from builder.models import Template
from .forms import AccordionForm
from .models import *


# View to create accordions
def accordionCreate(request):
    context = {}

    if request.method == 'POST':
        form = AccordionForm(request.POST)
        context['accordionForm'] = form

        if form.is_valid():
            template_id = request.POST.get('template')
            position = request.POST.get('position')
            template = get_object_or_404(Template, id=template_id)

            panel_nro = form.cleaned_data['panels']
            parent = form.save(commit=False)
            parent.template = template
            parent.position = position
            parent.save()

            for i in range(0, panel_nro):
                Accordion(
                    title='Panel hijo',
                    parent=parent
                ).save()

            context['success'] = True

            return render(request, 'create_accordion.html', context)

        # Error in form.
        return render(request, 'create_accordion.html', context)
    else:
        context['accordionForm'] = AccordionForm()
        context['template_id'] = request.GET.get('template')
        context['position'] = request.GET.get('position')

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
