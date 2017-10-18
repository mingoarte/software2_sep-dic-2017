from django.shortcuts import render
from django.http import HttpResponse
from uidesigner.audio_captcha import CaptchaAuditivo
from captcha.image import ImageCaptcha
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
