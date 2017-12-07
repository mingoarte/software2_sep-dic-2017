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
        time.sleep(5)
        driver.find_element_by_css_selector("li.collapsed").click()
        time.sleep(5)
        driver.find_element_by_link_text("NavBar").click()
        time.sleep(2)
        driver.find_element_by_id("navbarBrandName").clear()
        time.sleep(2)
        driver.find_element_by_id("navbarBrandName").send_keys("CEIC")
        time.sleep(2)
        driver.find_element_by_xpath("//button[@onclick=\"addElement('brand')\"]").click()
        time.sleep(2)
        Select(driver.find_element_by_id("elementList")).select_by_visible_text("Link")
        time.sleep(2)
        driver.find_element_by_id("linkName").clear()
        time.sleep(2)
        driver.find_element_by_id("linkName").send_keys("Home")
        time.sleep(2)
        driver.find_element_by_css_selector("button.button1").click()
        time.sleep(2)
        Select(driver.find_element_by_id("elementList")).select_by_visible_text("Dropdown")
        time.sleep(2)
        driver.find_element_by_id("dropdownName").clear()
        time.sleep(2)
        driver.find_element_by_id("dropdownName").send_keys(u"Información")
        time.sleep(2)
        driver.find_element_by_id("dropdownItem1").clear()
        time.sleep(2)
        driver.find_element_by_id("dropdownItem1").send_keys("Acerca de..")
        time.sleep(2)
        driver.find_element_by_css_selector("input.button1").click()
        time.sleep(2)
        driver.find_element_by_id("dropdownItem2").clear()
        time.sleep(2)
        driver.find_element_by_id("dropdownItem2").send_keys(u"Dirección")
        time.sleep(2)
        driver.find_element_by_xpath("//button[@onclick=\"addElement('dropdown')\"]").click()
        time.sleep(2)
        Select(driver.find_element_by_id("elementList")).select_by_visible_text("Link")
        time.sleep(2)
        Select(driver.find_element_by_id("linkOption")).select_by_visible_text("Deshabilitado")
        time.sleep(2)
        driver.find_element_by_id("linkName").clear()
        time.sleep(2)
        driver.find_element_by_id("linkName").send_keys("Notas")
        time.sleep(2)
        driver.find_element_by_css_selector("button.button1").click()
        time.sleep(2)
        driver.find_element_by_id("accept_keys").click()
        time.sleep(2)
        driver.find_element_by_id("frm1_submit").click()
        time.sleep(2)
        driver.find_element_by_id(u"Información").click()
        time.sleep(2)
        driver.find_element_by_link_text("<< Volver").click()

        # Configurar
        driver.find_element_by_xpath("//button[@type='button']").click()
        Select(driver.find_element_by_id("elementList")).select_by_visible_text("Link")
        time.sleep(2)
        driver.find_element_by_id("linkName").clear()
        time.sleep(2)
        driver.find_element_by_id("linkName").send_keys("Otros")
        time.sleep(2)
        driver.find_element_by_css_selector("button.button1").click()
        time.sleep(2)
        driver.find_element_by_id("accept_keys").click()
        time.sleep(2)
        driver.find_element_by_id("frm1_submit").click()
        time.sleep(2)
        driver.find_element_by_link_text("<< Volver").click()
        time.sleep(2)
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
