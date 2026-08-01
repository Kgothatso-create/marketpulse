from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Currency
from .services import get_exchange_rates


def display_exchange_rates(
    request: HttpRequest,
    base: str,
) -> HttpResponse:
    """
    Display exchange rates for a base currency.

    Args:
        request: The incoming HTTP request.
        base: The base currency code (e.g. "USD", "EUR", "ZAR").

    Returns:
        The rendered exchange rates page.
    """
    currency = get_object_or_404(Currency, code=base)

    exchange_rates = get_exchange_rates(base=currency.code)

    context = {
        "currency": currency,
        "exchange_rates": exchange_rates,
    }

    return render(request, "exchange_rates.html", context)
