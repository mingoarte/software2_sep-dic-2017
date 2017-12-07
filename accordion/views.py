#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, Http404
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import AccordionForm
from .models import *


# View to list accordions
def accordionList(request):
    return render(
        request,
        'list_accordion.html',
        context={
            'list': Accordion.objects.all(),
            'accordionForm': AccordionForm,
        }
    )


# View to create accordions
def accordionCreate(request):
    context = {}

    if request.method == 'POST':
        form = AccordionForm(request.POST)
        context['accordionForm'] = form
        print("En teoria fue post")

        if form.is_valid():
            panel_nro = form.cleaned_data['panels']
            parent = form.save()

            for i in range(0, panel_nro):
                Accordion(
                    title='Panel hijo',
                    parent=parent
                ).save()

            print("FUE VALIDO")
            return redirect('accordion:accordion-edit', question.pk)

        # Error in form.
        print("Fue post pero con error")
        return HttpResponse(json.dumps(form.errors), status=400)
    else:
        context['accordionForm'] = AccordionForm()

    print("VAMO A VER Q ES LO Q ES")
    return render(request, 'index.html', context, status=400)


# View to delete accordions
def accordionEdit(request, accordion_id):
    # Initialize context and search for accordion to edit
    try:
        accordion = Accordion.all_objects.get(accordion_id=accordion_id)
    except ObjectDoesNotExist:
        raise ObjectDoesNotExist()

    if request.method == 'POST':
        form = AccordionForm(request.POST or None, instance=accordion)
    elif request.method == 'GET':
        form = AccordionForm(request.GET or None, instance=accordion)
    else:
        raise Http404()

    if form.is_valid():
        form.save()

    return JsonResponse({'success':True})

def accordionModalEdit(request):
    if request.method == 'GET' and request.GET.get('acordeon-id','') :

        acordeon_id = request.GET['acordeon-id']

        try:
            accordion = Accordion.all_objects.get(accordion_id=acordeon_id)
        except ObjectDoesNotExist:
            raise Http404()

        accordionForm = AccordionForm(instance=accordion)


        return JsonResponse(
            data={
                'html':render_to_string(
                    'patrones/accordion/modal_editar_panel.html',
                    {"accordionForm": accordionForm}
                )
            }
        )

    raise Http404()

# View to delete accordions
def accordionDelete(request, accordion_id):
    # Get accordion to delete and delete it
    if request.method == 'GET':
        try:
            accordion = Accordion.all_objects.get(accordion_id=accordion_id)
        except ObjectDoesNotExist:
            raise ObjectDoesNotExist()
        accordion.delete()

        if request.is_ajax():
            return JsonResponse({'success':True})

    return redirect('accordion:accordion-list')
