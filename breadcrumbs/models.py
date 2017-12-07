from django.db import models

from builder.models import Pattern
from django.template.loader import render_to_string
from django.forms import inlineformset_factory


# Create your models here.
class Breadcrumb(Pattern):
    name = 'breadcrumb'

    title = models.CharField(max_length=30, default="Breadcrumb")

    def render(self):
        return render_to_string('patrones/breadcrumbs/view.html', {"pattern": self})

    def render_config_modal(self, request):
        return rendering_form(self, request)
        #return render_to_string('breadcrumbs/configurar-modal.html', {"pattern": self})

    def render_card(self):
        return render_to_string('patrones/breadcrumbs/build.html', {"pattern": self})

    def content(self):
        return self.breadcrumbcontent_set.all()

class BreadcrumbContent(models.Model):
    title = models.CharField(max_length=30)
    url = models.URLField()
    breadcrumb = models.ForeignKey(Breadcrumb, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

def rendering_form(breadcrumb, request):
    from .forms import BreadcrumbsForm

    ContentInlineFormSet = inlineformset_factory(
        Breadcrumb, BreadcrumbContent, fields=('title', 'url'), extra=2)

    form = BreadcrumbsForm(instance=breadcrumb)
    formset = ContentInlineFormSet(instance=breadcrumb)
    return render_to_string(
        template_name='breadcrumbs/configurar-modal.html',
        context={'formset': formset, 'form': form, 'breadcrumb': breadcrumb},
        request=request
    )
