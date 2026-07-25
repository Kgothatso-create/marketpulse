import requests
from datetime import datetime
from typing import Any


def get_current_weather(location: Any) -> dict:
    """
    Retrieve the current weather data for a given location.

    This service calls the Open-Meteo API using the location's latitude
    and longitude, then formats the current weather information for use
    within the application templates.

    Args:
        location (Any): Object containing latitude and longitude attributes.

    Returns:
        dict: Current weather details including temperature, humidity,
        wind speed, formatted date/time, and hourly temperature data.
    """

    # Open-Meteo weather API endpoint
    url = "https://api.open-meteo.com/v1/forecast"

    # API parameters defining location and required weather data
    params = {
        "latitude": location.latitude,
        "longitude": location.longitude,
        "current": [
            "temperature_2m",
            "relative_humidity_2m",
            "apparent_temperature",
            "weather_code",
            "wind_speed_10m",
        ],
        "hourly": "temperature_2m",
        "timezone": "auto",
    }

    # Make API request and raise an exception for failed responses
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

    # Convert API datetime string into a Python datetime object
    current_datetime = datetime.fromisoformat(
        data["current"]["time"]
    )

    return {
        "temperature": data["current"]["temperature_2m"],
        "humidity": data["current"]["relative_humidity_2m"],
        "feels_like": data["current"]["apparent_temperature"],
        "wind_speed": data["current"]["wind_speed_10m"],
        "weather_code": data["current"]["weather_code"],
        "timezone": data["timezone"],
        "current_time": current_datetime.strftime("%H:%M"),
        "current_date": current_datetime.strftime("%d %B %Y"),
        "hourly": list(
            zip(
                data["hourly"]["time"],
                data["hourly"]["temperature_2m"],
            )
        ),
    }


def get_weeks_weather(location: Any) -> dict:
    """
    Retrieve the upcoming weather forecast for a given location.

    This service retrieves daily weather data from the Open-Meteo API.
    The forecast excludes the current day and returns the following
    three days with formatted dates, maximum temperatures, minimum
    temperatures, and weather codes.

    Args:
        location (Any): Object containing latitude and longitude attributes.

    Returns:
        dict: Three-day weather forecast data.
    """

    # Open-Meteo weather API endpoint
    url = "https://api.open-meteo.com/v1/forecast"

    # API parameters defining location and daily forecast data required
    params = {
        "latitude": location.latitude,
        "longitude": location.longitude,
        "current": [
            "temperature_2m",
            "relative_humidity_2m",
            "apparent_temperature",
            "wind_speed_10m",
            "weather_code",
        ],
        "daily": [
            "weather_code",
            "temperature_2m_max",
            "temperature_2m_min",
            "sunrise",
            "sunset",
        ],
        "timezone": "auto",
    }

    # Make API request and raise an exception for failed responses
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

    # Exclude today's forecast and only return the next three days
    forecast_dates = [
        datetime.fromisoformat(date).strftime("%d %B %Y")
        for date in data["daily"]["time"][1:4]
    ]

    return {
        "forecast": list(
            zip(
                forecast_dates,
                data["daily"]["temperature_2m_max"][1:4],
                data["daily"]["temperature_2m_min"][1:4],
                data["daily"]["weather_code"][1:4],
            )
        )
    }