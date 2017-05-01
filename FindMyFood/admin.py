from django.contrib import admin
from django.contrib.gis import admin


# Register your models here.
from FindMyFood.models import Users, geoData

admin.site.register(Users)
admin.site.register(geoData)