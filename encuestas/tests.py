# -*- coding: utf-8 -*-
import unittest
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from django.urls import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

class ControlPollTest(StaticLiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

class TestCamposVacios(ControlPollTest):
    #@unittest.skip("Verificada")
    def runTest(self):
        self.driver.get('%s%s' % (self.live_server_url, '/encuestas/new/'))
        self.driver.find_element_by_id("check").click()
        self.driver.find_element_by_id("create").send_keys(Keys.RETURN)
        self.assertTrue(u"" in self.driver.page_source)

class TestDosOpciones(ControlPollTest):
    #@unittest.skip("Verificada")
    def runTest(self):
        self.driver.get('%s%s' % (self.live_server_url, '/encuestas/new/'))
        self.submit = self.driver.find_element_by_id("create")
        self.confirm_pregs = self.driver.find_element_by_id("check")
        self.text_preg = self.driver.find_element_by_id("id_texto_pregunta")
        self.text_op1 = self.driver.find_element_by_id("id_form-0-texto_opcion")
        self.text_op2 = self.driver.find_element_by_id("id_form-1-texto_opcion")
        self.text_preg.send_keys("Pregunta de Encuesta?")
        self.text_op1.send_keys("Opcion 1")
        self.text_op2.send_keys("Opcion 2")
        self.confirm_pregs.click()
        self.submit.send_keys(Keys.RETURN)
        self.assertTrue(u"Opcion 1" in self.driver.page_source)
        self.assertTrue(u"Opcion 2" in self.driver.page_source)

class TestTresOpciones(ControlPollTest):
  #@unittest.skip("Verificada")
    def runTest(self):
        self.driver.get('%s%s' % (self.live_server_url, '/encuestas/new/'))
        self.submit = self.driver.find_element_by_id("create")
        self.confirm_pregs = self.driver.find_element_by_id("check")
        self.add_more = self.driver.find_element_by_id("add_more")
        self.add_more.click()
        self.text_preg = self.driver.find_element_by_id("id_texto_pregunta")
        self.text_op1 = self.driver.find_element_by_id("id_form-0-texto_opcion")
        self.text_op2 = self.driver.find_element_by_id("id_form-1-texto_opcion")
        self.text_op3 = self.driver.find_element_by_id("id_form-2-texto_opcion")
        self.text_preg.send_keys("Pregunta de Encuesta?")
        self.text_op1.send_keys("Opcion 1")
        self.text_op2.send_keys("Opcion 2")
        self.text_op3.send_keys("Opcion 3")
        self.confirm_pregs.click()
        self.submit.send_keys(Keys.RETURN)
        self.assertTrue(u"Opcion 1" in self.driver.page_source)
        self.assertTrue(u"Opcion 2" in self.driver.page_source)
        self.assertTrue(u"Opcion 3" in self.driver.page_source)

class TestVotarEncuesta(ControlPollTest):
    #@unittest.skip("Verificada")
    def runTest(self):
        # Crear
        self.driver.get('%s%s' % (self.live_server_url, '/encuestas/new/'))
        self.submit = self.driver.find_element_by_id("create")
        self.confirm_pregs = self.driver.find_element_by_id("check")
        self.add_more = self.driver.find_element_by_id("add_more")
        self.add_more.click()
        self.text_preg = self.driver.find_element_by_id("id_texto_pregunta")
        self.text_op1 = self.driver.find_element_by_id("id_form-0-texto_opcion")
        self.text_op2 = self.driver.find_element_by_id("id_form-1-texto_opcion")
        self.text_op3 = self.driver.find_element_by_id("id_form-2-texto_opcion")
        self.text_preg.send_keys("Pregunta de Encuesta?")
        self.text_op1.send_keys("Opcion 1")
        self.text_op2.send_keys("Opcion 2")
        self.text_op3.send_keys("Opcion 3")
        self.confirm_pregs.click()
        self.submit.send_keys(Keys.RETURN)
        self.assertTrue(u"Opcion 1" in self.driver.page_source)
        self.assertTrue(u"Opcion 2" in self.driver.page_source)
        self.assertTrue(u"Opcion 3" in self.driver.page_source)

        # Votar
        self.opcion = self.driver.find_element_by_id("choice1")
        self.opcion.click()
        self.confirm_pregs = self.driver.find_element_by_id("check")
        self.confirm_pregs.click()
        self.votar = self.driver.find_element_by_id("vote")
        self.votar.click()
        self.assertTrue(u"¡Gracias por participar!" in self.driver.page_source)
        self.assertTrue(u"1 voto" in self.driver.page_source)

if __name__ == '__main__':
    unittest.main()