from django.shortcuts import render
from django.http import HttpResponse

from app.forms import WeatherDataForm
from utils.load_to_db import save_forecast_details

# Create your views here.


def ping(request):
    # ping service
    return HttpResponse("Pong")


def index(request):
    if request.method == "POST":
        form = WeatherDataForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form_obj = form.save()
            save_forecast_details(form_obj)

            return render(
                request, "app/index.html", {"form": form, "msg": "Loaded successfully !!!"}
            )
    else:
        form = WeatherDataForm()
    return render(request, "app/index.html", {"form": form})
