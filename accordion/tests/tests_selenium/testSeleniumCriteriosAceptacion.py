from selenium.webdriver.support.ui import Select
from selenium import webdriver
from time import sleep
from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.webdriver import WebDriver
from accordion.models import Accordion

class TestSeleniumCriteriosAceptacion(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super(TestSeleniumCriteriosAceptacion, cls).setUpClass()
        cls.selenium = webdriver.Firefox()
        cls.selenium.implicitly_wait(0)

        cls.user = User.objects.create_user('manuggz', 'manuelggonzalezm@gmail.com', 'pass')

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(TestSeleniumCriteriosAceptacion, cls).tearDownClass()

    def moverseA(self,nueva_url):
        url_anterior = self.selenium.current_url

        self.selenium.get('%s%s' % (self.live_server_url, nueva_url))

        while url_anterior == self.selenium.current_url:
            sleep(1)

        self.assertEqual(self.selenium.current_url, '%s%s' % (self.live_server_url, nueva_url))

    def iniciar_sesion(self):

        self.moverseA('/login/')

        form = self.selenium.find_element_by_css_selector('form')

        form.find_element_by_name('username').send_keys('manuggz')
        form.find_element_by_name('password').send_keys('pass')

        url_anterior = self.selenium.current_url

        form.find_element_by_css_selector('button[type="submit"]').click()

        while url_anterior == self.selenium.current_url:
            sleep(1)

        self.assertEqual(self.selenium.current_url, '%s%s' % (self.live_server_url, '/'))

        enlace_logout = self.selenium.find_element_by_css_selector("a[href='/logout/']")

    def disenyar(self):

        self.moverseA('/builder/build/')

        self.selenium.find_element_by_name('template_name').send_keys('Test Acordeon')

        self.selenium.find_element_by_id('accept_name_template').click()

        self.selenium.find_element_by_css_selector("li[data-target='#builder-form-btn']").click()

        self.selenium.find_element_by_css_selector('.pattern.pattern-accordion').click()

    def test_criterio_crear_acordeon(self):
        "Prueba que un usuario pueda crear un acordeon"

        self.selenium.get('%s%s' % (self.live_server_url, '/'))

        self.iniciar_sesion()

        self.disenyar()

        # enl_modal = self.selenium.find_element_by_css_selector('[data-target="#minesweep-create-modal"]')
        # enl_modal.click()  # Click al enlace para abrir el modal
        #
        # acordeon_mdl = Accordion(
        #     tooltip="tooltip",
        #     tooltip_style="tooltip_style",
        #     content="<img src='/static/img/objeto1.png'>",
        #     content_style="content_style",
        #     width="123",
        #     height="987",
        #     tooltip_side='bottom',
        # )
        # # minesweep_mdl.save()
        #
        # form_crear_minesweep = self.selenium.find_element_by_css_selector('form#minesweep-create-form')
        #
        # form_crear_minesweep.find_element_by_name('tooltip').send_keys(minesweep_mdl.tooltip)
        # form_crear_minesweep.find_element_by_name('tooltip_style').send_keys(minesweep_mdl.tooltip_style)
        # form_crear_minesweep.find_element_by_name('content').send_keys(minesweep_mdl.content)
        # form_crear_minesweep.find_element_by_name('content_style').send_keys(minesweep_mdl.content_style)
        #
        # select =  Select(form_crear_minesweep.find_element_by_name('tooltip_side'))
        # select.select_by_value(minesweep_mdl.tooltip_side)
        #
        # form_crear_minesweep.find_element_by_name('width').clear()
        # form_crear_minesweep.find_element_by_name('width').send_keys(minesweep_mdl.width)
        #
        # form_crear_minesweep.find_element_by_name('height').clear()
        # form_crear_minesweep.find_element_by_name('height').send_keys(minesweep_mdl.height)
        #
        # # Guardamos la url actual del usuario antes de crear el minesweep
        # url_antes_guardar_minesweep = self.selenium.current_url
        #
        # form_crear_minesweep.find_element_by_css_selector('button[type="submit"]').click()
        #
        # # Mientrasque no se haya redirido a la vista donde se muestra el minesweep creado
        # while url_antes_guardar_minesweep == self.selenium.current_url:
        #     sleep(1)
        #
        # self.assertEqual(self.selenium.current_url, '%s%s' % (self.live_server_url, '/minesweep/'))
        #
        # minesweep_mdl_bd = Minesweep.objects.get(tooltip="tooltip")
        #
        # self.assertEqual(minesweep_mdl.tooltip,       minesweep_mdl_bd.tooltip)
        # self.assertEqual(minesweep_mdl.tooltip_style, minesweep_mdl_bd.tooltip_style)
        # self.assertEqual(minesweep_mdl.content,       minesweep_mdl_bd.content)
        # self.assertEqual(minesweep_mdl.content_style, minesweep_mdl_bd.content_style)
        # self.assertEqual(minesweep_mdl.width,         minesweep_mdl_bd.width)
        # self.assertEqual(minesweep_mdl.height,        minesweep_mdl_bd.height)
        # self.assertEqual(minesweep_mdl.tooltip_side,        minesweep_mdl_bd.tooltip_side)
        #
        # # Faltaría verificar que la preview del minesweep está bien hecha
        #
        # self.assertEqual(self.selenium.find_element_by_css_selector(
        #     'div[data-tooltip-content="#minesweep-' + str(minesweep_mdl_bd.minesweep_id) + '"] img').get_attribute('src'), self.live_server_url + '/static/img/objeto1.png')

