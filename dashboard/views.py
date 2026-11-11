
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
    currency = Currency.objects.get(code="ZAR")

    context = {
        "location": location,
        "current_weather": get_current_weather(location),
        "weeks_weather": get_weeks_weather(location),
        "currency": currency,
        "exchange_rates": get_exchange_rates(currency.code),
    }

    return render(request, "index.html", context)
