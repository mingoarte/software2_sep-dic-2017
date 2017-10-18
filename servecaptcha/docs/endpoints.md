# Documentación sobre los endpoints provistos.
En el presente documento se detallará las características y operaciones realizadas por cada endpoint provisto para el manejo de los captchas.

## Generación de un APIKEY.
- Acceso: método GET.
- URL: /servecaptcha/generate_apikey/

- Entrada: Ninguna

- Acciones:
	- Crea un APIKEY para el diseñador.

- Retorna: la clave pública del APIKEY.

## Generación de un CAPTCHA.
- Acceso: método GET.
- URL: /servecaptcha/generate_captcha/public_key/

- Entrada: 
	- Llave pública del CAPTCHA en public_key

- Acciones:
	- Buscar el APIKEY asociado a la llave pública.
	- Generar aleatoriamente una respuesta.
	- Generar un CAPTCHA asociando la respuesta con el APIKEY.

- Retorna: Respuesta correcta del CAPTCHA creado en la BD.

## Validación de un CAPTCHA.
- Acceso: método POST.
- URL: /servecaptcha/validate_captcha/

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