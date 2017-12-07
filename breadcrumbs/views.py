from django.forms import inlineformset_factory
from django.http import JsonResponse
from django.shortcuts import render

from builder.models import Template, TemplateComponent

from .forms import ContentForm, BreadcrumbsForm
from .models import BreadcrumbContent, Breadcrumb


def BreadcrumbConfig(request):
    breadcrumb = Breadcrumb()

    ContentInlineFormSet = inlineformset_factory(
        Breadcrumb, BreadcrumbContent, fields=('title', 'url'), extra=2)

    if request.method == "POST":
        template_id = request.POST.get("template", None)
        position = request.POST.get("position", None)
        isNew = False

        if position is None:
            template = Template.objects.get(pk=int(template_id))
            patterns = template.sorted_patterns()

            if patterns:
                position = patterns[-1].template_component.get().position + 1
            else:
                position = 0

            isNew = True
        else:
            template = Template.objects.get(pk=int(template_id))
            component = TemplateComponent.objects.get(position=int(position), template=template)
            breadcrumb = Breadcrumb.objects.get(template_component=component)

        form = BreadcrumbsForm(request.POST, instance=breadcrumb)
        if form.is_valid():
            created_breadcrumb = form.save(commit=False)
            formset = ContentInlineFormSet(
                request.POST, instance=created_breadcrumb)
            if formset.is_valid():
                created_breadcrumb.save()
                if isNew:
                    TemplateComponent.objects.create(
                        content_object=created_breadcrumb, 
                        template_id=int(template_id), 
                        position=position
                    )
                formset.save()
                return JsonResponse({
                    'position': breadcrumb.template_component.get().position,
                    'html': breadcrumb.render_card()
                })
    else:
        template_id = request.GET.get("template", None)
        position = request.GET.get("position", None)

        if position is None:
            template = Template.objects.get(pk=int(template_id))
            patterns = template.sorted_patterns()

            if patterns:
                position = patterns[-1].template_component.get().position + 1
            else:
                position = 0

        form = BreadcrumbsForm(instance=breadcrumb)
        formset = ContentInlineFormSet(instance=breadcrumb)
    return render(request, 'breadcrumbs/configurar-modal.html', {'formset': formset, 'form': form, 'breadcrumb': breadcrumb})
