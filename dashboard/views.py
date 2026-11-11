
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from weather.models import Location
from weather.services import (
    get_current_weather,
    get_weeks_weather,
)

from exchangerate.models import Currency
from exchangerate.services import get_exchange_rates


def index(request: HttpRequest) -> HttpResponse:
    """
    Display the MarketPulse dashboard.

    Args:
        request: The incoming HTTP request.

    Returns:
        The rendered dashboard page.
    """
    location = Location.objects.get(city="Polokwane")
    locations = Location.objects.all()
    currency = Currency.objects.get(code="ZAR")
    currencies = Currency.objects.all()

    context = {
        "location": location,
        "locations": locations,
        "current_weather": get_current_weather(location),
        "weeks_weather": get_weeks_weather(location),
        "currency": currency,
        "currencies": currencies,
        "exchange_rates": get_exchange_rates(currency.code),
    }

    return render(request, "index.html", context)


def road_map(request: HttpRequest) -> HttpResponse:
    """
    Display the MarketPulse roadmap.

    Args:
        request: The incoming HTTP request.

    Returns:
        The rendered roadmap page.
    """
    return render(request, "road_map.html")
