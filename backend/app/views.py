from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def ping(request):
    
    return HttpResponse("Pong")

def index(request):
    # return HttpResponse("Hello, world. You're at the app index.")
    return render(request, 'app/index.html', {})

