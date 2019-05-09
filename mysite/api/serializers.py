from rest_framework import serializers
from api.models import User


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    surname = serializers.CharField(required=True)
    e_mail = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    phone_n = serializers.CharField(required=True)
    country = serializers.CharField(required=True)
    city = serializers.CharField(required=True)
    street = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('id', 'name', 'surname', 'e_mail', 'password', 'phone_n', 'country', 'city', 'street')