from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def Welcome(request):
    r = requests.get('http://127.0.0.1:5000/')
    print( r.json()) 
    respuesta = r.json()
    return HttpResponse("<h1>Welcome msg = "+respuesta['MSG']+"</h1><textarea/>")

