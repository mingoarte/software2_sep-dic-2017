from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.urls import reverse
from django.utils.html import escape
import json
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
		'generated_html': escape(html),
		'generated_js': escape(js),
		'generated_css': escape(css),
	}
	return render(request, 'tuisd/generatedCode.html', context)

def demoCaptcha(request):
	return render(request, 'tuisd/captcha/demo.html')
