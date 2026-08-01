import requests


def get_exchange_rates(base: str) -> dict:
    """
    Retrieve exchange rates for a base currency.

    Args:
        base: The base currency code (e.g. "USD", "EUR", "ZAR").

    Returns:
        The JSON response from the Frankfurter API.
    """
    url = f"https://api.frankfurter.dev/v2/rates?base={base}"

    response = requests.get(url)
    response.raise_for_status()

    return response.json()