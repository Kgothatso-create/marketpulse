from django.contrib.admin import register
from django.contrib import admin

from weather.models import Location


@register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("city", "latitude", "longitude")
    search_fields = ("city",)