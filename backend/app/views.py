from django.shortcuts import render
from django.http import HttpResponse

from app.forms import WeatherDataForm

# Create your views here.

def ping(request):
    # ping service
    return HttpResponse("Pong")

def index(request):
    if request.method == 'POST':
        form = WeatherDataForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form_obj = form.save()
            return render(request, 'app/index.html', {'form': form})
    else:
        form = WeatherDataForm()
    return render(request, 'app/index.html', {'form': form})
