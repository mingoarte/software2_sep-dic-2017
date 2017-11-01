# [CI4712] Tools of User Interfaces Design centered in Interaction Patterns (TUIsD)

Este repositorio contiene la implementación del código para el proyecto del trimestre Septiembre - Diciembre 2017 del curso CI4712 Ingeniería de Software II, en la Universidad Simón Bolívar.

El proyecto consistió en la implementación de diferentes patrones de interacción y la utilización de éstos a través del diseño de páginas web.

Cuatro equipos conformaron el desarrollo:
- JSWeCan
- PowerSoft
- Phoenix
- Otro equipo

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

### [Probar solamente el constructor]
```bash
cd software2_sep-dic-2017
python3 -m venv constructor
source constructor/bin/activate
pip3 install -r requirements_constructor.txt
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
```

(Luego deberiamos ponernos de acuerdo para hacer esto de una mejor manera, las claves no deberian estar en el repo)

## Ejecución del proyecto

### Primera ejecución
Se deben efectuar las migraciones a la BD para crear las tablas de las distintas aplicaciones.
```bash
cd software2_sep-dic-2017
python manage.py makemigrations
```
