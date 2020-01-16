from django.contrib import admin
# from leaflet.admin import LeafletGeoAdmin
from airmap.models import Monitor, Reading

admin.site.register(Monitor)
admin.site.register(Reading)
