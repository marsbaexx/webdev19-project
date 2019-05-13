from api.models import Database
from api.serializers import DatabaseSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from django.contrib.auth.models import Database
# from rest_framework.authtoken.models import
from rest_framework.decorators import api_view
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class DatabaseList(generics.ListAPIView):
    queryset = Database.objects.all()
    serializer_class = DatabaseSerializer
    permission_classes = (IsAuthenticated,)

class DatabaseDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Database.objects.all()
    serializer_class = DatabaseSerializer2


