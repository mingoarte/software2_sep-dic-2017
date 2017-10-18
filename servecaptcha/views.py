from django.shortcuts import render
from django.http import HttpResponse
from uidesigner.audio_captcha import CaptchaAuditivo
from captcha.image import ImageCaptcha
import random


def serveCaptchaImage(request):
    
    image = ImageCaptcha()
    data = image.generate('%s' % random.randint(0,99999))

    response = HttpResponse(data, content_type="image/png")
    return response

# Sirve el archivo .wav pero al parecer está corrupto. Leí que primero hay que guardarlo y despues servirlo
def serveCaptchaAudio(request):
    
    audio = CaptchaAuditivo()
    data = audio.generate('%s' % random.randint(0,99999))

    response = HttpResponse(data, content_type="audio/wav")
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
	pass

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