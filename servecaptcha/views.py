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
