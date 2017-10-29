from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, Http404, JsonResponse


def index(request):
	return render(request, 'formBuilder/index.html')
