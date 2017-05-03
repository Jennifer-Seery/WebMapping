from rest_framework import serializers
from .models import geoData
from .models import Users

#serialising the user data
class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


#serialsing the geodata information.
class GeoDBSerializer(serializers.ModelSerializer):
    class Meta:
        model = geoData
        fields = '__all__'