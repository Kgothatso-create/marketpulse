import requests


def get_exchange_rates(base: str) -> list[dict]:
    """
    Retrieve exchange rates for a base currency.
    Documentation: https://frankfurter.dev/

    Args:
        base: The base currency code (e.g. "USD", "EUR", "ZAR").

    Returns:
        A list of exchange rate records.
    """
    url = "https://api.frankfurter.dev/v2/rates"

    response = requests.get(
        url,
        params={"base": base},
        timeout=10,
    )
    response.raise_for_status()

    return response.json()
