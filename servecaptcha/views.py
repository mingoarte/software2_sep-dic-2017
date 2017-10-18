from django.shortcuts import render
from django.http import HttpResponse
from captcha.audio import AudioCaptcha
from captcha.image import ImageCaptcha
import random


def serveCaptchaImage(request):
    
    image = ImageCaptcha()
    data = image.generate('%s' % random.randint(0,99999))

    response = HttpResponse(data, content_type="image/png")
    return response
