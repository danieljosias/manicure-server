from rest_framework import serializers
from .models import Admin
from users.serializers import UserSerializer
from users.models import User


class AdminSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Admin
        fields = ['id', 'user']
        read_only_fields = ['id']

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user = User.objects.create_user(**user_data)
        validated_data["user"] = user

        admin = Admin.objects.create(**validated_data)

        return admin
