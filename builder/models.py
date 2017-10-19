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


class Pattern(models.Model):
	name = models.CharField(max_length=128)

	def __str__(self):
		return self.name
