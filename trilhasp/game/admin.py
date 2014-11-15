from django.contrib import admin

# Register your models here.
from models import *

admin.site.register(GameCoinModel)
admin.site.register(GameFinances)
admin.site.register(BusBrands)
admin.site.register(GameBusModel)
admin.site.register(GameBusAvailability)
admin.site.register(GamePersonalBusFleet)
