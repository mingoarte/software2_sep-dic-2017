from django.db import models
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
import os


def get_user_path(username):
	return os.path.join('uploads/templates', username)


class Template(models.Model):
	# user = models.OneToOneField(User)
	# html = models.FileField(upload_to="uploads/")
	name = models.CharField(max_length=128, default="")
	created_at = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

	def sorted_patterns(self):
		patterns = self.questions() + self.forms()
		return sorted(patterns, key = lambda p: p.position)

	def forms(self):
		# TODO: Obtener forms del template
		return []

	def questions(self):
		patterns = []
		questions = Pregunta.objects.filter(template=template)
		for question in questions:
			patterns.append({
				'question': question,
				'options': Opcion.objects.filter(pregunta=question),
				'position': question.position
			})
		return patterns


class Pattern(models.Model):
	name = models.CharField(max_length=128)

	def __str__(self):
		return self.name

# Los componentes que forman parte del template implementan este modelo abstracto
class TemplateComponent(models.Model):
    position = models.IntegerField(null=True)
    template = models.ForeignKey(Template, null=True)

    class Meta:
        abstract = True
