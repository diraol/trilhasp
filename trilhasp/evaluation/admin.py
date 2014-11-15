from django.contrib.gis import admin

# Register your models here.
from models import *


class MyOSMGeoAdmin(admin.OSMGeoAdmin):
    default_lat = -2701590.32734
    default_lon = -5192099.80109
    default_zoom = 12
    map_width = 800

admin.site.register(EVALQuestion)
admin.site.register(EVALAnswer, MyOSMGeoAdmin)
admin.site.register(EVALAnswerModel)
admin.site.register(Buses)
admin.site.register(BusLine)
admin.site.register(BusCompanies)
