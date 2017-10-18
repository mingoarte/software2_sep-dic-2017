from django.shortcuts import render
from django.http import HttpResponse
from uidesigner.audio_captcha import CaptchaAuditivo
from captcha.image import ImageCaptcha
import random

def serveCaptchaImage(request, name):
    
    image = ImageCaptcha()
    #data = image.generate('%s' % name)
    image.write('%s' % name, 'static/%s.png' % name)

    #response = HttpResponse(data, content_type="image/png")
    #return response

def serveCaptchaAudio(request, name):
    
    audio = CaptchaAuditivo()
    #data = audio.generate()
    audio.write('%s' % name, 'static/%s.mp3' % name)
    #return render(request, 'servecaptcha/index.html')

def serveCaptcha(request):
    name = random.randint(0,99999)

    serveCaptchaAudio(request, name)
    serveCaptchaImage(request, name)

    return render(request, 'servecaptcha/index.html', {'name': name})
