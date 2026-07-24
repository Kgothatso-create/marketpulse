import requests
from weather.models import Location


def get_current_weather(location):
    """
    This service gets the current weather.
    """

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": location.latitude,
        "longitude": location.longitude,
        "hourly": "temperature_2m",
    }

    response = requests.get(url, params=params, timeout=10, verify=False)
    response.raise_for_status()
    print(response.json())
    return response.json()
