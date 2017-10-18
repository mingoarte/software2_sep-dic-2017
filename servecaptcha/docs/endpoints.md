# Documentación sobre los endpoints provistos.
En el presente documento se detallará las características y operaciones realizadas por cada endpoint provisto para el manejo de los captchas.

## Generación de un CAPTCHA.
- Acceso: método GET.

- Entrada: 
	- Llave pública del CAPTCHA.

- Acciones:
	- Buscar el APIKEY asociado a la llave pública.
	- Generar imagen de CAPTCHA.
	- Generar sonido de CAPTCHA.
	- Generar un CAPTCHA asociando el texto de la imagen como respuesta y el APIKEY.

- Retorna: Respuesta correcta del CAPTCHA creado en la BD.

## Validación de un CAPTCHA.
- Acceso: método POST.

- Entrada:
	- Respuesta del usuario.
	- CAPTCHAID.
	- LLave pública asociada al CAPTCHA.

- Acciones:
	- Verificar que el formulario sea válido.
	- Buscar el CAPTCHA dentro de la BD con el CAPTCHAID.
	- Buscar el APIKEY asociado el CAPTCHA dentro de la BD con la llave pública.
	- Verificar que la respuesta del usuario sea la que corresponde en el CAPTCHA.
	- Verificar que el APIKEY buscado en la BD sea el mismo al asociado al CAPTCHA.

- Retorna: Es válido o no el CAPTCHA con la información pasada.