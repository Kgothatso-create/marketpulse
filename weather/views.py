from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from weather.models import Location
from weather.services import get_current_weather, get_weeks_weather


def current_weather(request: HttpRequest) -> HttpResponse:
    """
    Display the current weather information for the configured location.

    Retrieves the location data from the database, fetches current weather
    conditions and the upcoming forecast through the weather services, and
    passes the data to the weather template.

    Args:
        request (HttpRequest): Incoming HTTP request.

    Returns:
        HttpResponse: Rendered weather page response.
    """

    # Retrieve the location for which weather information is displayed
    location = Location.objects.get(city="Polokwane")

    # Gather weather data required by the template
    context = {
        "location": location,
        "current_weather": get_current_weather(location),
        "weeks_weather": get_weeks_weather(location),
    }

    # Render the weather page with the collected context data
    return render(request, "current_weather.html", context)
