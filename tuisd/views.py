from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	context = {}
	return render(request, 'tuisd/index.html', context)

def showCaptcha(request):
	context = {}
	return render(request, 'tuisd/showCaptcha.html', context)


def showCaptchaCode(request):
	context = {}
	return render(request, 'tuisd/generatedCode.html', context)
