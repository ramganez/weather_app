import json

from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.http import JsonResponse

from app.forms import WeatherDataForm
from utils.load_to_db import save_forecast_details
from utils.search_query import select_days, select_days_with_time
from utils.utils import separate_date_time


# Create your views here.


def ping(request):
    # ping service
    return HttpResponse("Pong")


def index(request):
    """backend Landing Page where admin add upload the data"""

    if request.method == "POST":
        form = WeatherDataForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form_obj = form.save()
            save_forecast_details(form_obj)

            return render(
                request,
                "app/index.html",
                {"form": form, "msg": "Loaded successfully !!!"},
            )
    else:
        form = WeatherDataForm()
    return render(request, "app/index.html", {"form": form})


def weekly(request):
    """Fetch weekly weather data"""
    if request.method == "POST":
        query = json.loads(request.body)["query"]  #'2022-10-07 15:00'
        withTime = json.loads(request.body)["withTime"]
        if withTime:
            results = select_days_with_time(query)
        else:
            results = select_days(query)
        serialized = serializers.serialize("python", results)
        result_list = [d["fields"] for d in serialized]
        final_results = separate_date_time(result_list)
        return JsonResponse(final_results, safe=False)
