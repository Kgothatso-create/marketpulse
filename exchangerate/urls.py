from django.urls import path

from . import views

app_name = "exchangerate"

urlpatterns = [
    path(
        "rates/<str:base>/", views.display_exchange_rates, name="display_exchange_rates",
    ),
]
