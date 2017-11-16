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

## Cómo crear un nuevo patrón?
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

Para crear una nueva instancia de un patrón, puedes utilizar el método create_pattern, que recibe los atributos de MiPatron, así como `template` y `position` para crear el TemplateComponent automaticamente. Este método devuelve la instancia creada


