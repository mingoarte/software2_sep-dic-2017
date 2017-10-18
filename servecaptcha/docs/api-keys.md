# Documentación sobre la generación de llaves para el usuario.
Por cómo se diseñó el patrón de interacción CAPTCHA, se tiene que generar una llave pública 
y una llave privada que esté asociada 

## Función para generación de strings.
Dentro de la carpeta de `utils` se encuentra el script `random_string.py` que contiene la función que genera de manera aleatoria un string de tamaño (por defecto) de 64 caracteres, que pueden ser letras en minúsculas, mayúsculas y dígitos. 

## Generación de llaves públicas y privadas (APIKEY)
En la definición del modelo se tiene una tabla que contiene la definición de un APIKEY. 

EL objeto Key-Pair tiene las siguientes variables:
- public_key: representa la llave pública.
- private_key: representa la llave privada.

Para nosotros el APIKEY se refiere a la tupla (PublicK, PrivateK), donde en la primera posición se tiene la llave pública que se le da al usuario al momento de generar una en el sistema, en la seguna posición se tiene la llave privada que es mantenida en el servidor y sirve para validar la llave pública entregada al usuario.

Ambas llaves tienen las siguientes propiedades:
- Longitud máxima: 64 caracteres.
- Son únicas.
- Si no se entrega una llave pública/privada en el constructor, el sistema crea una utilizando la función `alphanumeric` de `random_string.py`.

Un diseñador para poder incluir un CAPTCHA en su página primero debe generar un APIKEY a través del endpoint provisto. El diseñador puede escoger la creación de varios APIKEY.


## Generación de identificador de CAPTCHA (CAPTCHAID)

Cuando se realiza una petición de generación de un CAPTCHA, el endpoint crea uns instancia de un `GeneratedCaptcha` que se muestra en `models.py`. 

Estos objetos tienen las siguientes variables:
- id: identificador numérico dentro del manejador de base de datos.
- captcha_id: campo de caracteres que representa el identificador del captcha para el endpoint y que se enviará al diseñador al momento de generarlo.
- keypair: Referencia a una instancia de Key-Pair que contiene el APIKEY del diseñador.
- answer: la respuesta correcta para validar el CAPTCHA por parte del usuario final.

