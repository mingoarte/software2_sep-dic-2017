# -*- coding: utf-8 -*-
import unittest
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from django.urls import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from faqs.models import *

class ControlFAQTest(StaticLiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('%s%s' % (self.live_server_url, '/faqs/new/'))
        self.submit = self.driver.find_element_by_id("create")
        self.confirm_pregs = self.driver.find_element_by_id("check")
        self.add_more = self.driver.find_element_by_id("add_more")
        self.confirm_tema = self.driver.find_element_by_id("tema_check")

    def tearDown(self):
        self.driver.close()

class TestCamposVacios(ControlFAQTest):
    #@unittest.skip("Verificada")
    def runTest(self):
        self.confirm_pregs.click()
        self.submit.send_keys(Keys.RETURN)
        self.assertTrue(u"This field is required." in self.driver.page_source)

class TestRespuestaVacia(ControlFAQTest):
    #@unittest.skip("Verificada")
    def runTest(self):
        self.text_preg = self.driver.find_element_by_id("id_form-0-pregunta")
        self.text_preg.send_keys("Pregunta1?")
        self.confirm_pregs.click()
        self.submit.send_keys(Keys.RETURN)
        self.assertTrue(u"This field is required." in self.driver.page_source)

class TestPreguntaVacia(ControlFAQTest):
    #@unittest.skip("Verificada")
    def runTest(self):
        self.text_resp = self.driver.find_element_by_id("id_form-0-respuesta")
        self.text_resp.send_keys("Respuesta1")
        self.confirm_pregs.click()
        self.submit.send_keys(Keys.RETURN)
        self.assertTrue(u"This field is required." in self.driver.page_source)

class TestUnaPreguntaRespuesta(ControlFAQTest):
    #@unittest.skip("Verificada")
    def runTest(self):
        self.text_preg = self.driver.find_element_by_id("id_form-0-pregunta")
        self.text_resp = self.driver.find_element_by_id("id_form-0-respuesta")
        self.text_preg.send_keys("Pregunta1?")
        self.text_resp.send_keys("Respuesta1")
        self.confirm_pregs.click()
        self.submit.send_keys(Keys.RETURN)
        self.assertTrue(u"Pregunta1?" in self.driver.page_source)
        self.assertTrue(u"Respuesta1" in self.driver.page_source)

class TestUnaPreguntaRespuestaConTema(ControlFAQTest):
    #@unittest.skip("Verificada")
    def runTest(self):
        self.confirm_tema.click()
        self.driver.find_element_by_id("id_nombre").send_keys("Tema1")
        self.text_preg = self.driver.find_element_by_id("id_form-0-pregunta")
        self.text_resp = self.driver.find_element_by_id("id_form-0-respuesta")
        self.text_preg.send_keys("Pregunta1?")
        self.text_resp.send_keys("Respuesta1")
        self.confirm_pregs.click()
        self.submit.send_keys(Keys.RETURN)
        self.assertTrue(u"Pregunta1?" in self.driver.page_source)
        self.assertTrue(u"Respuesta1" in self.driver.page_source)
        self.assertTrue(u"Tema1" in self.driver.page_source)


#if __name__ == '__main__':
    #unittest.main()

class ModelsTestCase(TestCase):

    def setUp(self):

        # Valores de setteo.

        # Hoy
        hoy = datetime.now(timezone.utc)

        # Valores para variar las fechas.
        day1 = timedelta(days=1)
        day2 = timedelta(days=20)
        day3 = timedelta(days=3)
        day4 = timedelta(days=2)
        day5 = timedelta(days=17)
        day6 = timedelta(days=8)

        # FAQS DE PRUEBA

        self.faq1 = Faq.objects.create(
            name = "faq1",
            fecha_creacion = hoy+day1,
        )

        self.faq2 = Faq.objects.create(
            name = "faq2",
            fecha_creacion = hoy+day2,
        )

        self.faq3 = Faq.objects.create(
            name = "faq3",
            fecha_creacion = hoy+day3,
        )

        # CATEGORIAS DE PRUEBA

        self.categ1 = Categoria.objects.create(
            faq = self.faq1,
            nombre = "categoria1",
            fecha_publ = hoy+day4,
        )

        self.categ2 = Categoria.objects.create(
            faq = self.faq2,
            nombre = "categoria2",
            fecha_publ = hoy+day5,
        )

        self.categ3 = Categoria.objects.create(
            faq = self.faq3,
            nombre = "categoria3",
            fecha_publ = hoy+day6,
        )

        # PREGUNTAS DE PRUEBA.

        self.preg1 = PreguntaFaq.objects.create(
            faq = self.faq1,
            tema = self.categ1,
            pregunta = "¿Cómo instalar Ubuntu mediante un pendrive?",
            respuesta = "Usar Rufus, bootear desde el pendrive y seguir los pasos.",
        )

        self.preg2 = PreguntaFaq.objects.create(
            faq = self.faq2,
            tema = self.categ2,
            pregunta = "¿Cómo sobrevivir en la USB?",
            respuesta = "Fajándose.",
        )

        self.preg3 = PreguntaFaq.objects.create(
            faq = self.faq3,
            tema = self.categ3,
            pregunta = "¿Cómo hacer capturas de pantalla en Ubuntu?",
            respuesta = "Presionar el botón ImprPant.",
        )

        # PRUEBAS UNITARIAS

        # PRUEBAS DE LA CLASE "Faq"

        # Se prueba el campo 'name''y su correctitud.
        def test_name(self):
            self.assertEqual(self.faq1.name, "faq1")
            self.assertEqual(self.faq2.name, "faq2")
            self.assertEqual(self.faq3.name, "faq3")

        # Se prueba el campo 'fecha_creacion' y su correctitud.
        def test_fecha_creacion(self):
            self.assertLess(self.faq1.fecha_creacion, datetime.now(timezone.utc))
            self.assertLess(self.faq2.fecha_creacion, datetime.now(timezone.utc))
            self.assertLess(self.faq3.fecha_creacion, datetime.now(timezone.utc))

        # Se prueba el método 'es_reciente' y su correcto funcionamiento.
        def test_pregunta_es_reciente(self):
            self.assertEqual(self.faq1.es_reciente(), True)
            self.assertEqual(self.faq2.es_reciente(), True)
            self.assertEqual(self.faq3.es_reciente(), True)

        # Se prueba el método 'categoria' y su correcto funcionamiento.
        def test_categoria(self):
            self.assertEqual(self.categ1, faq1.categoria())
            self.assertEqual(self.categ2, faq2.categoria())
            self.assertEqual(self.categ3, faq3.categoria())

        # PRUEBAS DE LA CLASE "Categoria"

        # Se prueba el campo 'nombre' y su correctitud.
        def test_nombre(self):
            self.assertEqual(self.categ1.nombre, "categoria1")
            self.assertEqual(self.categ2.nombre, "categoria2")
            self.assertEqual(self.categ3.nombre, "categoria3")

        # Se prueba el campo 'fecha_publ' y su correctitud.
        def test_fecha_publicacion(self):
            self.assertLess(self.categ1.fecha_publ, datetime.now(timezone.utc))
            self.assertLess(self.categ2.fecha_publ, datetime.now(timezone.utc))
            self.assertLess(self.categ3.fecha_publ, datetime.now(timezone.utc))

        # Se prueba el método '__str__' y su correcto funcionamiento.
        def test_str_method_categoria(self):
            self.assertEqual(self.categ1.nombre, self.categ1.__str__())
            self.assertEqual(self.categ2.nombre, self.categ2.__str__())
            self.assertEqual(self.categ3.nombre, self.categ3.__str__())

        # PRUEBAS DE LA CLASE "PreguntaFaq"

        # Se prueba el campo 'faq' y su correctitud.
        def test_preg_faq(self):
            self.assertEqual(self.preg1.faq, self.faq1)
            self.assertEqual(self.preg2.faq, self.faq2)
            self.assertEqual(self.preg3.faq, self.faq3)

        # Se prueba el campo 'tema' y su correctitud.
        def test_preg_categ(self):
            self.assertEqual(self.preg1.tema, self.categ1)
            self.assertEqual(self.preg2.tema, self.categ2)
            self.assertEqual(self.preg3.tema, self.categ3)

        # Se prueba el campo 'pregunta' y su correctitud.
        def test_preg_pregunta(self):
            self.assertEqual(self.preg1.pregunta, "¿Cómo instalar Ubuntu mediante un pendrive?")
            self.assertEqual(self.preg2.pregunta, "¿Cómo sobrevivir en la USB?")
            self.assertEqual(self.preg3.pregunta, "¿Cómo hacer capturas de pantalla en Ubuntu?")

        # Se prueba el campo 'respuesta' y su correctitud.
        def test_preg_respuesta(self):
            self.assertEqual(self.preg1.respuesta, "Usar Rufus, bootear desde el pendrive y seguir los pasos.")
            self.assertEqual(self.preg2.respuesta, "Fajándose.")
            self.assertEqual(self.preg3.respuesta, "Presionar el botón ImprPant.")

        # Se prueba el método '__str__' y su correcto funcionamiento.
        def test_str_method_pregunta(self):
            self.assertEqual(self.preg1.pregunta, self.preg1.__str__())
            self.assertEqual(self.preg2.pregunta, self.preg2.__str__())
            self.assertEqual(self.preg3.pregunta, self.preg3.__str__())        