from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Users
from .models import geoData
from .serializers import UsersSerializer
from .serializers import GeoDBSerializer

class UsersList(APIView):
    def get(self, request):
        users = Users.objects.all()
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class GeoDBList(APIView):
    def get(self, request):
        geodb = geoData.objects.all()
        serializer1 = GeoDBSerializer(geodb, many=True)
        return Response(serializer1.data)

    def post(self):
        pass
