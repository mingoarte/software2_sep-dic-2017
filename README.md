# TUIsD
Repositorio para el proyecto de Ingeniería de Software II Sep-Dic 2017

Este repositorio contiene la implementación del código para el proyecto del trimestre Septiembre - Diciembre 2017 del curso CI4712 Ingeniería de Software II, en la Universidad Simón Bolívar.

El proyecto consistió en la implementación de diferentes patrones de interacción y la utilización de éstos a través del diseño de páginas web.

Cuatro equipos conformaron el desarrollo:
- JSWeCan
- NineSoft
- Phoenix
- PowerSoft

## Requisitos de la instalación en Linux
El proyecto fue desarrollado utilizando Django como framework y PostgreSQL como manejador de base de datos relacionales.

- Python3
- Pip3
- Postgresql

### Instalación de dependencias
Se procede a instalar Pip3 y Virtualenv.
``` bash
sudo apt-get -y install python3-pip python3-venv
```

### Instalación de requerimientos
Para instalar el proyecto, debes clonar el proyecto, crear un ambiente virtual e instalar las dependencias, para ello ejecuta los siguientes comandos:

``` bash
cd software2_sep-dic-2017
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
```

## Configuración de la BD.

### Instalación de PostgreSQL.
Si no tienes instalado Postgres en tu computadora, sigue esta guía: https://www.digitalocean.com/community/tutorials/como-instalar-y-utilizar-postgresql-en-ubuntu-16-04-es

### Configuración
Se debe crear un usuario llamado `tuisd`, con clave `tuisd` y con el nombre de la base de datos `tuisd`.

```bash
sudo -u postgres psql
create user tuisd with password 'tuisd';
create database tuisd owner tuisd;
alter user tuisd CREATEDB;
```

(Luego deberiamos ponernos de acuerdo para hacer esto de una mejor manera, las claves no deberian estar en el repo)

## Ejecución del proyecto

### Primera ejecución
Se deben efectuar las migraciones a la BD para crear las tablas de las distintas aplicaciones.
```bash
cd software2_sep-dic-2017
python manage.py makemigrations <nombre_app_django>
python manage.py migrate
```

Si no hubo problemas al migrar, se procede a ejecutar el servidor.
```bash
python manage.py runserver localhost:8000
```

# Cómo crear un nuevo patrón?
Para crear un nuevo patrón debes definir su modelo, que implementa el modelo abstracto Patron y defina un método render que devuelva el HTML que corresponde a ese patrón.
Ejemplo:

```python
from builder.models import Patron
class MiPatron(Patron):
    # ... mis atributos

    # Este método devuelve el html que corresponde a la visualización del patrón
    def render(self):
        pass
```

Para crear una nueva instancia de un patrón, puedes utilizar el método create_pattern, que recibe los atributos de MiPatron, así como `template` y `position` para crear el TemplateComponent automaticamente. Este método devuelve la instancia creada.

El método render edevuelve el html que se debe mostrar en el card. Por consistencia
este archivo debe estar localizado en `TUIsD/templates/patrones/<nombre_patron>/build.html`.

## Inclusión en la barra lateral izquierda.
La barra izquierda se encuentra en `TUIsD/templates/builder/sidebar.html`. Para
agregar un patrón a esta barra debe incluirse lo siguiente dentro de la lista
con id `products` y poniendo como ejemplo el captcha:
```html
    <li class="pattern-captcha config"><a href="#">CAPTCHA</a></li>
```

De manera abstracta:
```html
    <li class="pattern-{nombre_patrón} config"><a href="#">{nombre_patrón}</a></li>
```

Lo siguiente que debe incluirse son las funciones en JS que permitan configurar
el patrón, específicamente, deben agregarse al bloque `custom_scripts` que está
en `TUIsD/templates/builder/build.html` el archivo JS que abre la configuración
del patrón con un modal, como ejemplo captcha:
```html
<script type="text/javascript" src="{% static 'js/builder-captcha.js' %}"></script>
```

Por consistencia en el proyecto, estos builder deben localizarse SIEMPRE en
`TUIsD/static/js/`.

Por último, en `TUIsD/templates/builder/build.html` debe incluirse justo antes
de cerrar el div de `builder_content` el archivo en html que contiene la
configuración del modal. Este archivo contiene todo el código en HTML que le
será incluido al modal cuando se haga clic en el patrón en la barra lateral o
al darle clic al botón de configurar. Por ejemplo:
```html
{% include 'patrones/captcha_pattern/configurar-modal.html' %}
```

Por consistencia en el proyecto, este archivo debe llamarse SIEMPRE en
`TUIsD/templates/patrones/<nombre_patrón>/configurar-modal.html`

## Aceptar las configuraciones hechas al patrón en el modal.
Para poder enviar todo lo configurado en el modal a a la base de datos, debe
configurarse el botón de `aceptar` del mismo para que tome las variables que
necesite y las envíe.

Esta función recibirá, si es la primera vez que se crea un patrón, la posición y
debe ser debidamente añadida.

Esta función debe estar en `builder-<nombre_patrón>.js`.
Por consistencia, debe hacer un request a `../<nombre_patrón>-config/`. Como
parte de los datos siempre deben ir `'template': $('#template_id').val()` y
`position': $('#position').val(),`.

## Para configurar el botón de elimado de un patrón.
Para eliminar un patrón, debe definirse una vista en `builder/urls.py` y `builder/views.py`,
por consistencia, este request se hace al view `../erase-<nombre_patrón>/`.

Los datos obligatorios que debe tener esta llamada es `template` y `position`,
que representan el id del template y la posición, respectivamente.
