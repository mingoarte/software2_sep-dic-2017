# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Captcha(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_captcha(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_link_text(u"Iniciar Sesión").click()
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("alejandra21")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("A12345678")
        driver.find_element_by_css_selector("button.btn.btn-primary").click()
        driver.find_element_by_link_text(u"Diseño").click()
        driver.find_element_by_id("template_name").clear()
        driver.find_element_by_id("template_name").send_keys("Prueba5")
        driver.find_element_by_id("accept_name_template").click()
        time.sleep(2)
        driver.find_element_by_css_selector("li.collapsed").click()
        time.sleep(2)
        driver.find_element_by_link_text("Formulario").click()
        time.sleep(2)
        # Titulo
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div[2]/div/div/div/div[2]/div/div/div[2]/ul/li[6]").click()
        time.sleep(2)
        # Autocompletar
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div[2]/div/div/div/div[2]/div/div/div[2]/ul/li[1]").click()
        time.sleep(2)
        # Area de texto
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div[2]/div/div/div/div[2]/div/div/div[2]/ul/li[13]").click()
        time.sleep(2)
        # Boton
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div[2]/div/div/div/div[2]/div/div/div[2]/ul/li[2]").click()
        time.sleep(2)
        # Aceptar
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div[2]/div/div/div/div[3]/button[1]").click()
        time.sleep(2)
        # Configurar
        driver.find_element_by_xpath("(//button[@type='button'])[8]").click()
        time.sleep(2)
        #Eliminar campo de autocompletar
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div[2]/div/div/div/div[2]/div/div/div[1]/ul/li[2]/div[1]/a[1]").click()
        time.sleep(2)
        # Editar boton de submit
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div[2]/div/div/div/div[2]/div/div/div[1]/ul/li[3]/div[1]/a[2]").click()
        time.sleep(2)
        # Se colorea el boton de azul
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div[2]/div/div/div/div[2]/div/div/div[1]/ul/li[3]/div[3]/div/div[3]/div/button[3]").click()
        time.sleep(2)
        # Cerramos la ventana de edicion
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div[2]/div/div/div/div[2]/div/div/div[1]/ul/li[3]/div[3]/div/a").click()
        time.sleep(2)
        # Aceptamos
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div[2]/div/div/div/div[3]/button[1]").click()
        time.sleep(2)
        #Preview
        driver.find_element_by_id("frm1_submit").click()
        time.sleep(2)
        driver.find_element_by_link_text("<< Volver").click()
        time.sleep(2)
        # Se elimina el formulario
        driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
        time.sleep(2)

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
