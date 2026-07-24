from django.http import JsonResponse
from django.shortcuts import render
from weather.models import Location
from weather.services import get_current_weather


# Create your views here.
def current_weather(request):

    location = Location.objects.get(city="Polokwane")

    current_weather = get_current_weather(location)

    return JsonResponse(current_weather)
