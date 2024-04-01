from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(min_length=8)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    date_joined = serializers.DateTimeField(read_only=True,)
    last_login = serializers.DateTimeField(read_only=True)

    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'last_name', "date_joined", "last_login", "email"]

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)

     