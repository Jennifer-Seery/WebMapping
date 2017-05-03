from django.contrib import admin
from django.contrib.gis import admin


# Register your models here.
from FindMyFood.models import Users, geoData

#registering the models on the admin page
admin.site.register(Users)
admin.site.register(geoData)