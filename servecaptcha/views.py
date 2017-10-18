from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, Http404
from uidesigner.audio_captcha import CaptchaAuditivo
from captcha.image import ImageCaptcha
from .models import KeyPair, GeneratedCaptcha
import random


def serveCaptchaImage(request, name):
    image = ImageCaptcha()
    image.write('%s' % name, 'static/%s.png' % name)

    # Descomentar estas dos líneas hace que al ir a localhost/servecaptcha/image, 
    # se muestre una imagen en el navegador con el captcha generado
    # Hay que proporcionarle un valor como primer argumento a image.write para que 
    # cree la imagen

    #data = image.generate('%s' % name)
    #response = HttpResponse(data, content_type="image/png")


def serveCaptchaAudio(request, name):
    audio = CaptchaAuditivo()
    audio.write('%s' % name, 'static/%s.mp3' % name)

    # Misma acotación de arriba

    #return render(request, 'servecaptcha/index.html')

def serveCaptcha(request):
    name = random.randint(0,99999)

    serveCaptchaAudio(request, name)
    serveCaptchaImage(request, name)

    return render(request, 'servecaptcha/index.html', {'name': name})
    #response = HttpResponse(data, content_type="audio/wav")
    #return response

def generate_apikey(request):
	""" Función del endpoint para la generación de una APIKEY a través del método GET.

		Argumentos:
			request: Django request.

		Retorna:
			Un HTTP response OK con la llave pública del APIKEY. Error si algún
			campo no es correcto. 
	"""
	if request.method == 'GET':
		apikey = KeyPair()
		apikey.save()

		response = HttpResponse(content="{}".format(apikey.public_key))
	
	else:
		# Especificamos los métodos que acepta el endpoint.
		response = HttpResponseNotAllowed(content="Sólo se permite el método GET.", permitted_methods=["GET"])

	return response


def generate_captcha(request, public_key: str):
	""" Función del endpoint para la generación del CAPTCHA.
	
		Se recibe a través del URL la llave pública del CAPTCHA que se quiere generar.
		Esta llave se busca y si es encontrada genera un CAPTCHA aleatorio asociando
		el APIKEY a éste.

		Argumentos:
			request: Django request.
			public_key: string representando la llave pública del diseñador que incluyó
			            el CAPTCHA.

		Retorna:
			Un HTTP response OK con la respuesta correcta del CAPTCHA, error si algún
			campo no es correcto.
	"""
	if request.method == 'GET':
		# Como las llaves públicas son únicas, podemos utilizar el método get para 
		# obtener de la BD la única instancia que debe haber, sin embargo, 
		# este método puede lanzar una excepción si no se encuentra la llave pública.
		try:
			keypair = KeyPair.objects.get(public_key=public_key)
		except KeyPair.DoesNotExist:
			# return HttpResponseNotAllowed(content=["POST"])
			raise Http404("Llave pública no existe.") 

		respuesta_captcha = str(random.randint(0,999999))

		captcha = GeneratedCaptcha(keypair=keypair, answer=respuesta_captcha)
		captcha.save()

		response = HttpResponse(content="{}".format(respuesta_captcha))

	else:
		# Especificamos los métodos que acepta el endpoint.
		response = HttpResponseNotAllowed(content="Sólo se permite el método GET.", permitted_methods=["GET"])

	return response

def validate_captcha(request):
	""" Funcíón del endpoint para la validación del CAPTCHA.

		Se recibe por el método POST la llave pública del CAPTCHA, el CAPTCHAID y
		la respuesta ingresada por el usuario. Seguidamente se verifica que el 
		formulario sea válido según como se define en el documento de endpoints.

		Argumentos:
			request: Django request.
			captchaid: string que representa el CAPTCHAID.
			public_key: string que representa la llave pública del diseñador que 
					    incluyó el captcha.
			user_answer: string que representa la respuesta del usuario al responder
						 el captcha.

		Retorna:
			Un HTTP response OK si el captcha es válido, error en caso contrario.

	"""
	pass

