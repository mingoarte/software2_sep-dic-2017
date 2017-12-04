# -*- coding: utf-8 -*-

from django.test import TestCase
from builder.models import *
from datetime import datetime, timedelta
from django.utils import timezone

# Suite de pruebas para el 'builder' (constructor).

class ModelsTestCase(TestCase):

	def setUp(self):

		# Hoy
		today = datetime.now(timezone.utc)

		# Valores para variar las fechas.
		days1 = timedelta(days=1)
		days2 = timedelta(hours=20)
		days3 = timedelta(days=3)

		# TEMPLATES DE PRUEBA (para completar las preguntas).

		self.template1 = Template.objects.create(
			name = "Template 1",
			created_at = today,
			last_modified = today+days1,
		)

		self.template2 = Template.objects.create(
			name = "Template 2",
			created_at = today,
			last_modified = today+days2,
		)

		self.template3 = Template.objects.create(
			name = "Template 3",
			created_at = today,
			last_modified = today+days3,
		)

		# PATTERNS DE PRUEBA.

		#self.pattern1 = Pattern.objects.create(
		#	name = "Encuesta",
		#)

		#self.pattern2 = Pattern.objects.create(
		#	name = "Acordeón",
		#)

		#self.pattern3 = Pattern.objects.create(
		#	name = "Captcha",
		#)

	# PRUEBAS UNITARIAS

	# PRUBAS DE LA CLASE "Template".

	# Se prueba el campo 'name' y su correctitud.
	def test_name(self):
		self.assertEqual(self.template1.name, "Template 1")
		self.assertEqual(self.template2.name, "Template 2")
		self.assertEqual(self.template3.name, "Template 3")

	# Se prueba el campo 'created_at' y su correctitud.
	def test_created_at(self):
		self.assertLess(self.template1.created_at, datetime.now(timezone.utc))
		self.assertLess(self.template2.created_at, datetime.now(timezone.utc))
		self.assertLess(self.template3.created_at, datetime.now(timezone.utc))

	# Se prueba el campo 'last_modified' y su correctitud.
	def test_last_modified(self):
		self.assertLess(self.template1.last_modified, datetime.now(timezone.utc)+timedelta(days=1))
		self.assertLess(self.template2.last_modified, datetime.now(timezone.utc)+timedelta(hours=20))
		self.assertLess(self.template3.last_modified, datetime.now(timezone.utc)+timedelta(days=3))

	# Se prueba el método '__str__' y su correcto funcionamiento.
	def test_str_method_template(self):
		self.assertEqual(self.template1.name, self.template1.__str__())
		self.assertEqual(self.template2.name, self.template2.__str__())
		self.assertEqual(self.template3.name, self.template3.__str__())

	# PRUEBAS DE LA CLASE "Pattern".

	# Se prueba el campo 'name' y su correctitud.
	#def test_name_pattern(self):
	#	self.assertEqual(self.pattern1.name, "Encuesta")
	#	self.assertEqual(self.pattern2.name, "Acordeón")
	#	self.assertEqual(self.pattern3.name, "Captcha")

	# Se prueba el método '__str__' y su correcto funcionamiento.
	#def test_str_method_pattern(self):
	#	self.assertEqual(self.pattern1.name, self.pattern1.__str__())
	#	self.assertEqual(self.pattern2.name, self.pattern2.__str__())
	#	self.assertEqual(self.pattern3.name, self.pattern3.__str__())