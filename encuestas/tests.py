# -*- coding: utf-8 -*-

from django.test import TestCase
from encuestas.models import *
from builder.models import Template
from datetime import datetime, timedelta
from django.utils import timezone

# Suite de pruebas para el control "Encuestas".

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

		# PREGUNTAS DE PRUEBA.

		self.pregunta1 = Pregunta.objects.create(
			texto_pregunta = "¿Quién ganará El Clásico?",
			fecha_publ = datetime.now(timezone.utc),
			#template = self.template1
		)

		self.pregunta2 = Pregunta.objects.create(
			texto_pregunta = "¿Quién será el campeón de la Champions League?",
			fecha_publ = datetime.now(timezone.utc),
			#template = self.template2
		)

		self.pregunta3 = Pregunta.objects.create(
			texto_pregunta = "¿Pasaremos esta materia?",
			fecha_publ = datetime.now(timezone.utc),
			#template = self.template3
		)

		# OPCIONES DE PRUEBA.

		# Asociadas a la primera pregunta.

		self.opcion1_p1 = Opcion.objects.create(
			pregunta = self.pregunta1,
			texto_opcion = "Real Madrid",
			votos = 10,
		)

		self.opcion2_p1 = Opcion.objects.create(
			pregunta = self.pregunta1,
			texto_opcion = "FC Barcelona",
			votos = 12,
		)

		self.opcion3_p1 = Opcion.objects.create(
			pregunta = self.pregunta1,
			texto_opcion = "Empate",
			votos = 3,
		)

		# Asociadas a la segunda pregunta.

		self.opcion1_p2 = Opcion.objects.create(
			pregunta = self.pregunta2,
			texto_opcion = "Real Madrid",
			votos = 10,
		)

		self.opcion2_p2 = Opcion.objects.create(
			pregunta = self.pregunta2,
			texto_opcion = "FC Barcelona",
			votos = 12,
		)

		self.opcion3_p2 = Opcion.objects.create(
			pregunta = self.pregunta2,
			texto_opcion = "PSG",
			votos = 3,
		)

		# Asociadas a la tercera pregunta.

		self.opcion1_p3 = Opcion.objects.create(
			pregunta = self.pregunta3,
			texto_opcion = "Sí",
			votos = 10,
		)

		self.opcion2_p3 = Opcion.objects.create(
			pregunta = self.pregunta3,
			texto_opcion = "No",
			votos = 12,
		)

	# PRUEBAS UNITARIAS

	# PRUBAS DE LA CLASE "Pregunta".

	# Se prueba el campo 'texto_pregunta' y su correctitud.
	def test_texto_pregunta(self):
		self.assertEqual(self.pregunta1.texto_pregunta, "¿Quién ganará El Clásico?")
		self.assertEqual(self.pregunta2.texto_pregunta, "¿Quién será el campeón de la Champions League?")
		self.assertEqual(self.pregunta3.texto_pregunta, "¿Pasaremos esta materia?")

	# Se prueba el campo 'fecha_publ' y su correctitud.
	def test_fecha_publ(self):
		self.assertLess(self.pregunta1.fecha_publ, datetime.now(timezone.utc))
		self.assertLess(self.pregunta2.fecha_publ, datetime.now(timezone.utc))
		self.assertLess(self.pregunta3.fecha_publ, datetime.now(timezone.utc))

	# Se prueba el campo 'template' y su correctitud.
	#def test_template(self):
	#	self.assertEqual(self.pregunta1.template, self.template1)
	#	self.assertEqual(self.pregunta2.template, self.template2)
	#	self.assertEqual(self.pregunta3.template, self.template3)

	# Se prueba el método 'es_reciente' y su correcto funcionamiento.
	def test_pregunta_es_reciente(self):
		self.assertEqual(self.pregunta1.es_reciente(), True)
		self.assertEqual(self.pregunta2.es_reciente(), True)
		self.assertEqual(self.pregunta3.es_reciente(), True)

	# Se prueba el método '__str__' y su correcto funcionamiento.
	def test_str_method_pregunta(self):
		self.assertEqual(self.pregunta1.texto_pregunta, self.pregunta1.__str__())
		self.assertEqual(self.pregunta2.texto_pregunta, self.pregunta2.__str__())
		self.assertEqual(self.pregunta3.texto_pregunta, self.pregunta3.__str__())

	# PRUEBAS DE LA CLASE "Opcion".

	# Se prueba el campo 'pregunta' y su correctitud.
	def test_pregunta(self):
		self.assertEqual(self.opcion1_p1.pregunta, self.pregunta1)
		self.assertEqual(self.opcion2_p1.pregunta, self.pregunta1)
		self.assertEqual(self.opcion3_p1.pregunta, self.pregunta1)
		self.assertEqual(self.opcion1_p2.pregunta, self.pregunta2)
		self.assertEqual(self.opcion2_p2.pregunta, self.pregunta2)
		self.assertEqual(self.opcion3_p2.pregunta, self.pregunta2)
		self.assertEqual(self.opcion1_p3.pregunta, self.pregunta3)
		self.assertEqual(self.opcion2_p3.pregunta, self.pregunta3)

	# Se prueba el campo 'texto_opcion' y su correctitud.
	def test_texto_opcion(self):
		self.assertEqual(self.opcion1_p1.texto_opcion, "Real Madrid")
		self.assertEqual(self.opcion2_p1.texto_opcion, "FC Barcelona")
		self.assertEqual(self.opcion3_p1.texto_opcion, "Empate")
		self.assertEqual(self.opcion1_p2.texto_opcion, "Real Madrid")
		self.assertEqual(self.opcion2_p2.texto_opcion, "FC Barcelona")
		self.assertEqual(self.opcion3_p2.texto_opcion, "PSG")
		self.assertEqual(self.opcion1_p3.texto_opcion, "Sí")
		self.assertEqual(self.opcion2_p3.texto_opcion, "No")

	# Se prueba el campo 'votos' y su correctitud.
	def test_votos(self):
		self.assertEqual(self.opcion1_p1.votos, 10)
		self.assertEqual(self.opcion2_p1.votos, 12)
		self.assertEqual(self.opcion3_p1.votos, 3)
		self.assertEqual(self.opcion1_p2.votos, 10)
		self.assertEqual(self.opcion2_p2.votos, 12)
		self.assertEqual(self.opcion3_p2.votos, 3)
		self.assertEqual(self.opcion1_p3.votos, 10)
		self.assertEqual(self.opcion2_p3.votos, 12)

	# Se prueba el método '__str__' y su correcto funcionamiento.
	def test_str_method_opcion(self):
		self.assertEqual(self.opcion1_p1.texto_opcion, self.opcion1_p1.__str__())
		self.assertEqual(self.opcion2_p1.texto_opcion, self.opcion2_p1.__str__())
		self.assertEqual(self.opcion3_p1.texto_opcion, self.opcion3_p1.__str__())
		self.assertEqual(self.opcion1_p2.texto_opcion, self.opcion1_p2.__str__())
		self.assertEqual(self.opcion2_p2.texto_opcion, self.opcion2_p2.__str__())
		self.assertEqual(self.opcion3_p2.texto_opcion, self.opcion3_p2.__str__())
		self.assertEqual(self.opcion1_p3.texto_opcion, self.opcion1_p3.__str__())
		self.assertEqual(self.opcion2_p3.texto_opcion, self.opcion2_p3.__str__())