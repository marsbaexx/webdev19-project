from api.models import Admin
from api.serializers import AdminSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from django.contrib.auth.models import Admin
# from rest_framework.authtoken.models import
from rest_framework.decorators import api_view
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class AdminList(generics.ListAPIView):
    queryset = Admin.objects.all()
    serializer_class =AdminSerializer
    permission_classes = (IsAuthenticated,)

class AdminDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer2


@api_view(['POST'])
def AdminLogin(request):
    serializer = AuthTokenSerializer(data = request.data)
    serializer.is_valid(raise_exception=True)
    admin = serializer.validated_data.get('admin')
    token, created = Token.objects.get_or_create(admin = admin)

    return Response({'token': token.key})
@api_view(['POST'])
def UserLogout(request):
    print(type(request.auth))
    request.auth.delete()
    return Response('deleted')