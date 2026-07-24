from django.urls import path
from .views import *

namespace = "weather"

urlpatterns = [
    path('', current_weather, name='current_weather'),
]
