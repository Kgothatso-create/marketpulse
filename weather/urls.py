from django.urls import path
from . import views

app_name = "weather"

urlpatterns = [
    path('', views.current_weather, name='current_weather'),
    path("<str:city>/", views.detailed_weather, name="detailed_weather"),
]
