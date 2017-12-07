from django.contrib import admin
from .models import BreadcrumbContent, Breadcrumb

# Register your models here.
admin.site.register(BreadcrumbContent)
admin.site.register(Breadcrumb)
