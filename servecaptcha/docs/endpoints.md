# Documentación sobre los endpoints provistos.
En el presente documento se detallará las características y operaciones realizadas por cada endpoint provisto para el manejo de los captchas.

## Generación de un APIKEY.
- Acceso: método GET.
- URL: /servecaptcha/generate_apikey/

- Entrada: Ninguna

- Acciones:
	- Crea un APIKEY para el diseñador.

- Retorna: las claves publica y privadas para el diseñador

## Generación de un CAPTCHA.
- Acceso: método GET.
- URL: /servecaptcha/generate_captcha/public_key/

- Entrada:
	- Llave pública del diseñador en public_key

- Acciones:
	- Buscar el APIKEY asociado a la llave pública.
	- Generar aleatoriamente una respuesta.
	- Generar un CAPTCHA asociando la respuesta con el APIKEY.

- Retorna: ID del captcha creado.

## Validación de un CAPTCHA.
- Acceso: método POST.
- URL: /servecaptcha/validate_captcha/

- Entrada:
	- Respuesta del usuario.
	- CAPTCHAID.
	- LLave privada asociada al CAPTCHA.

- Acciones:
	- Verificar que el formulario sea válido.
	- Buscar el CAPTCHA dentro de la BD con el CAPTCHAID.
	- Buscar el APIKEY asociado el CAPTCHA dentro de la BD con la llave privada.
	- Verificar que la respuesta del usuario sea la que corresponde en el CAPTCHA.
	- Verificar que el APIKEY buscado en la BD sea el mismo al asociado al CAPTCHA.

- Retorna: Es válido o no el CAPTCHA con la información pasada.
