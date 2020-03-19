from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(style={'input_type': 'password'})

    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        fields = 'username', 'password', 'first_name', 'last_name', 'email'

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user