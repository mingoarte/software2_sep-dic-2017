import uuid
from django.db import models
from accordion.models import PatronAbstract

from django.db.models import CASCADE
from django.template.loader import render_to_string
from builder.models import Pattern, PatternManager


# Create your models here.
class TabContainer(models.Model):
    name = models.CharField(
        u'Nombre del container',
        max_length=100,
        null=True,
        blank=True
    )
    children_amount = models.IntegerField(
        u'Cantidad de pestañas',
        default=1
    )

    def __str__(self):
        return self.name


class Tab(PatronAbstract, Pattern):
    name = 'tab'

    parent = models.ForeignKey(
        TabContainer, on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    tab_id = models.UUIDField(
        u'Id del tab',
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(
        u'Titulo del tab',
        blank=True,
        null=True,
        max_length=100,
    )
    title_style = models.TextField(
        u'Estilos del titulo',
        blank=True,
        null=True
    )

    def __str__(self):
        return str(self.id)

    def get_uuid_as_str(self):
        return str(self.tab_id)

    def render(self):
        return render_to_string('patrones/tab/full_preview.html', {"tab": self})

    def render_card(self):
        return render_to_string(
            'patrones/tab/card_content_mini_preview.html',
            {"pattern": self}
        )

    def render_config_modal(self, request):
        from .forms import TabForm
        form = TabForm(instance=self)

        return render_to_string('patrones/tab/configurar-modal.html', {"tabForm": form})
