from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .inc import Ready, CPCGI

# Create your views here.
def success(request):
    return HttpResponse('Success')

def backurl(request):
    return HttpResponse('This is backURL')

def ready(request):
    return Ready.ready(request)

@csrf_exempt
def cpcgi(request):
    return CPCGI.cpcgi(request)