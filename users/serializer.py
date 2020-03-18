from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(style={'input_type': 'password'})

    class Meta:
        model = User
        fields = 'username', 'password', 'first_name', 'last_name', 'email'
