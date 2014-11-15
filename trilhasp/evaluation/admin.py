from django.contrib import admin

# Register your models here.
from models import *

admin.site.register(EVALQuestion)
admin.site.register(EVALAnswer)
admin.site.register(EVALAnswerModel)
admin.site.register(Buses)
admin.site.register(BusLine)
admin.site.register(BusCompanies)
