from django.db import models
#from django.contrib.gis.db import models

# Create your models here.

#If a system was to be implemented this would be the model used
class Users(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    bk = models.BooleanField()
    sub = models.BooleanField()
    tgi = models.BooleanField()
    mcD = models.BooleanField()
    KFC = models.BooleanField()


#model to hold all of the information about the locations of the restaurants
class geoData(models.Model):
    restname = models.CharField(max_length=40)
    locations = models.CharField(max_length=40)
    latitude = models.FloatField()
    longitude = models.FloatField()


def __str__(self):
        return self.name
