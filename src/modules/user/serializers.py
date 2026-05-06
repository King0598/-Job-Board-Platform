from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'role', 'phone', 'profile_picture', 'date_joined']
        read_only_fields = ['date_joined']

class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'role', 'phone']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user