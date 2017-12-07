from django.forms import ModelForm
from breadcrumbs.models import Breadcrumb, BreadcrumbContent

class BreadcrumbsForm(ModelForm):
    class Meta:
        model = Breadcrumb
        fields = ['title']
        labels = {
            'title': 'Título',
        }

class ContentForm(ModelForm):
    class Meta:
        model = BreadcrumbContent
        fields = ['title', 'url']
        labels = {
            'title': 'Título',
            'url': 'URL',
        }
