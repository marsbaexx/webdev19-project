from api.models import User
from api.serializers import UserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from api.models import Admin
from api.serializers import AdminSerializer
from api.models import Datebase
from api.serializers import AdminSerializer



class User(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class User_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class Admin(generics.ListCreateAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

class Admin_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

class Database(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class Database_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



