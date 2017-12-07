# -*- coding: utf-8 -*-
import uuid
from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE
from django.template.loader import render_to_string
from builder.models import Pattern, PatternManager


class BaseAccordionManager(PatternManager):

    def create_pattern(self, *args, **kwargs):
        # Extraer template_id y position de los argumentos
        template = kwargs.pop('template', None)
        if template:
            template_id = template.id
        elif 'template_id' in kwargs:
            template_id = kwargs.pop('template_id', None)

        position = kwargs.pop('position', 0)

        card_id = kwargs.pop('card-id', 0)

        # Crear patron y asignarle un TemplateComponent
        total_panels = kwargs.pop('panels', 0)

        parent = self.model(*args, **kwargs)
        parent.save()

        temp_c = parent.template_component.create(template_id=template_id, position=position)

        for i in range(0, int(total_panels)):
            accord_hijo = Accordion(
                title='Panel hijo',
                parent=parent
            )
            accord_hijo.save()
            print(accord_hijo)
            #accord_hijo.template_component = temp_c

        return parent

    def get_queryset(self):
        return super(BaseAccordionManager, self).get_queryset().filter(parent=None).order_by('id')


class PatronAbstract(models.Model):
    """docstring for ClassName"""
    content = models.TextField(
        u'Contenido',
        blank=True,
        null=True
    )
    content_color = models.CharField(
        u'Color del contenido',
        max_length=50,
        blank=True,
        null=True
    )
    content_style = models.TextField(
        u'Estilos del contenido',
        blank=True,
        null=True
    )
    border_style = models.TextField(
        u'Definir tipo de borde',
        blank=True,
        null=True
    )
    border_color = models.CharField(
        u'Color del borde',
        max_length=50,
        blank=True,
        null=True
    )
    border_radius = models.CharField(
        u'Radio del borde (px)',
        max_length=50,
        blank=True,
        null=True,
        default='0'
    )
    width = models.CharField(
        u'Ancho (%)',
        max_length=50,
        blank=True,
        null=True,
        default='100'
    )
    height = models.CharField(
        u'Alto (px)',
        max_length=50,
        blank=True,
        null=True,
        default='30'
    )
    style = models.TextField(
        u'Extra CSS',
        blank=True,
        null=True
    )

    class Meta:
        abstract = True

    def toHtml(self, template_name, var_name):
        return render_to_string(template_name, context={
            var_name: self,
        }
    )


class Accordion(PatronAbstract, Pattern):
    name = 'accordion'

    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='panels',
        on_delete=CASCADE
    )
    accordion_id = models.UUIDField(
        u'Id del acordeon',
        default=uuid.uuid4,
        editable=False
    )

    title = models.CharField(
        u'Título',
        max_length=50
    )
    title_style = models.TextField(
        u'Estilos del Título',
        blank=True,
        null=True
    )    

    # objects returns accordions that have no parent.
    # all_objects returns all accordions, with out without parents.
    objects = BaseAccordionManager()
    all_objects = models.Manager()

    def __str__(self):
        return str(self.id)

    def get_uuid_as_str(self):
        return str(self.accordion_id)

    def get_child_panels(self):
        panels = Accordion.all_objects.filter(parent=self.id).order_by('id')
        return panels

    def render(self):
        return render_to_string('patrones/accordion/full_preview.html', {"accordion": self})

    def render_card(self):
        return render_to_string(
            'patrones/accordion/card_content_mini_preview.html',
            {"pattern": self}
        )

    def render_config_modal(self, request):
        from .forms import AccordionForm
        form = AccordionForm(instance=self)

        return render_to_string('patrones/accordion/configurar-modal.html', {"accordionForm": form})

