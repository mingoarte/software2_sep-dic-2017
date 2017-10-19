from django.db import models
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
import os


def get_user_path(username):
	return os.path.join('uploads/templates', username)


class Template(models.Model):
	user = models.OneToOneField(User)
	html = models.FileField(upload_to="uploads/")
	created_at = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)


class Pattern(models.Model):
	name = models.CharField(max_length=128)



class Generic(models.Model):
	name = models.CharField(max_length=128)
	option1 = models.CharField(max_length=128, choices=(("Choice 1", "Choice 1"), ("Choice 2", "Choice 2")))
	option2 = models.CharField(max_length=128, choices=(("Choice 2.1", "Choice 2.1"), ("Choice 2.2", "Choice 2.2")))


class Pregunta(models.Model):
	ask = models.CharField(max_length=128)
	answer = models.CharField(max_length=2, choices=(("si", "Si"), ("no", "No")))
	encuesta = models.ForeignKey(Generic, related_name="preguntas", default=None)
