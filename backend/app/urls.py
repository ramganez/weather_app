from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('ping', views.ping, name='ping'),
    path('weekly', csrf_exempt(views.weekly), name='weekly'),
]