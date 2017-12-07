# Uso de Buildbot

1. Sigue las instrucciones en http://docs.buildbot.net/current/tutorial/firstrun.html para
instalar buildbot, y ejecutar un master y un worker local

2. Sustituye la configuración de tu master por la que esta provista aquí, y reinicialo.

3. Asegurate de estar ejecutando la aplicacion, como se indica en el README, y ya haber
hecho las migraciones necesarias.

4. Builbot esta configurado para monitorear la rama jswecan y ejecutar las pruebas
si detecta cambios. Puedes modificar el archivo de configuración para que ejecute más
pruebas o monitorear otras ramas.
