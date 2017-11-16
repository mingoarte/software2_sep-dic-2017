import json

from django.forms import model_to_dict, inlineformset_factory
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template.loader import get_template

from builder.models import Template, TemplateComponent
from .forms import CarouselForm
from .models import Carousel, Content

def CarouselConfig(request, pk=None):
    print("POST:", request.POST, "GET:", request.GET)
    if request.method == "POST":
        template_id = request.POST.get("template", None)
        position = request.POST.get("position", None)
    else:
        template_id = request.GET.get("template", None)
        position = request.GET.get("position", None)

    if pk is not None:
        carousel = Carousel.objects.get(pk=pk)
    else:
        carousel = Carousel()

    if position is None:
        template = Template.objects.get(pk=int(template_id))
        patterns = template.sorted_patterns()

        if patterns:
            position = patterns[-1].template_component.get().position
            position += 1
        else:
            position = 0

    ContentInlineFormSet = inlineformset_factory(Carousel, Content, fields=('title', 'description', 'image'), extra=2)

    if request.method == "POST":
        form = CarouselForm(request.POST, request.FILES, instance=carousel)
        if form.is_valid():
            created_carousel = form.save(commit=False)
            formset = ContentInlineFormSet(request.POST, request.FILES, instance=created_carousel)
            if formset.is_valid():
                created_carousel.save()
                TemplateComponent.objects.create(content_object=created_carousel, template_id=int(template_id), position=position)
                formset.save()
                return render(request, 'carrusel/carousel_create_success.html', {'carousel': carousel, 'position': position})
    else:
        form = CarouselForm(instance=carousel)
        formset = ContentInlineFormSet(instance=carousel)
    return render(request, 'carrusel/carousel_form.html', {'formset': formset, 'form': form, 'carousel': carousel})

def CarouselDelete(request):
    template = request.GET.get('template', None)
    position = request.GET.get('position', None)

    component = TemplateComponent.objects.filter(position=int(position), template_id=int(template))
    carousel = Carousel.objects.get(template_component=component)
    carousel.delete()

    return JsonResponse(data={})
