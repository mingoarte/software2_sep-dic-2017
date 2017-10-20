from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.urls import reverse
from django.utils.html import escape
from django.http import HttpResponse
from zipfile import ZipFile
import io
import json
import tempfile
import requests

def index(request):
    return render(request, 'tuisd/index.html')

def showCaptcha(request):
    return render(request, 'tuisd/showCaptcha.html')

def showCaptchaCode(request):
    keypair = requests.get('http://127.0.0.1:8000/servecaptcha/generate_apikey').json()
    html = render_to_string('tuisd/captcha/captcha.html', { 'public_key': keypair['public_key'] })
    js = render_to_string('tuisd/captcha/captcha.js', { 'public_key': keypair['public_key'] })
    with open('tuisd/static/tuisd/captcha/css/style.css') as f:
        css = f.read()

    context = {
        'public_key': keypair['public_key'],
        'private_key': keypair['private_key'],
        'html': escape(html),
        'js': escape(js),
        'css': escape(css),
    }
    return render(request, 'tuisd/generatedCode.html', context)

def generate_captcha_code_as_zip(request, public_key: str):
    html = render_to_string('tuisd/captcha/captcha_with_includes.html', { 'public_key': public_key })

    # Copio el contenido del zip base (con los recursos estaticos, CSS, JS) para
    # no modificar el archivo. ZipFile#writestr tiene side-effects
    with open('tuisd/static/tuisd/captcha/zip/captcha_base.zip', 'rb') as f:
        captcha_zip = io.BytesIO(f.read())

    with ZipFile(captcha_zip, 'a') as zipfile:
        zipfile.writestr('index.html', html)

    response = HttpResponse(captcha_zip.getbuffer(), content_type='application/x-zip-compressed')
    response['Content-disposition'] = 'attachment; filename="captcha.zip"'
    return response


def demoCaptcha(request):
    return render(request, 'tuisd/captcha/demo.html')
