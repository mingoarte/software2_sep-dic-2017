from django.db import models
from django.contrib.auth.models import User
import os

class Template(models.Model):
	user = models.OneToOneField(User)
	html = models.FileField(upload_to=get_user_path(self.user.username))
	created_at = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)


class Pattern(models.Model):
	name = models.CharField(max_length=128)


class Generic(models.Model):
	name = CharField(max_length=128)
	option1 = CharField(max_length=128, choices=(("Choice 1", "Choice 1"), ("Choice 2", "Choice 2")))
	option2 = CharField(max_length=128, choices=(("Choice 2.1", "Choice 2.1"), ("Choice 2.2", "Choice 2.2")))


def get_user_path(username):
	return os.path.join('uploads/templates', username)