from django.db import models
#from django.contrib.gis.db import models

# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    bk = models.BooleanField()
    sub = models.BooleanField()
    tgi = models.BooleanField()
    mcD = models.BooleanField()
    KFC = models.BooleanField()


class geoData(models.Model):
    restname = models.CharField(max_length=40)
    locations = models.CharField(max_length=40)
    latitude = models.FloatField()
    longitude = models.FloatField()


def __str__(self):
        return self.name
