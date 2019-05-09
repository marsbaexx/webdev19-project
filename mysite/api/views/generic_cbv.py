from api.models import User
from api.serializers import UserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404

class User(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class User_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
