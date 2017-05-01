from rest_framework import serializers
from .models import geoData
from .models import Users


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class GeoDBSerializer(serializers.ModelSerializer):
    class Meta:
        model = geoData
        fields = '__all__'