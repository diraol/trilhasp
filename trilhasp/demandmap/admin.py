from django.contrib import admin

# Register your models here.
from models import *

admin.site.register(GEOLastPosition)
admin.site.register(GEOHistoryPosition)
