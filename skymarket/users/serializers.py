import djoser.serializers
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer, UserSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class MyUserSerializer(UserSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "phone", "id", "email", "image"]


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "phone", "password", "email", "image"]


class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
