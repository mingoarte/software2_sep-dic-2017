# [CI4712] UI Designer

## Requisitos de la instalación

- Python 3
- Pip 3
- Postgresql

``` bash
sudo apt-get -y install python3-pip
```
- Virtual Env

``` bash
sudo apt-get install python3-venv
```

## Instalación

Para instalar el proyecto, debes clonar el proyecto, crear un ambiente virtual e instalar las dependencias, para ello ejecuta los siguientes comandos:

``` bash
cd ci4712-ui-designer
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
```

## Base de datos

Si no tienes instalado Postgres en tu computadora, sigue esta guia: https://www.digitalocean.com/community/tutorials/como-instalar-y-utilizar-postgresql-en-ubuntu-16-04-es

Crea un usuario llamado tuisd, con clave tuisd y una base de datos del mismo nombre
(Luego deberiamos ponernos de acuerdo para hacer esto de una mejor manera, las claves
no deberian estar en el repo)
