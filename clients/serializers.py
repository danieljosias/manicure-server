from rest_framework import serializers
from .models import Client
from users.models import User
from django.shortcuts import get_object_or_404
from users.serializers import UserSerializer


class ClientSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.UUIDField(write_only=True)
    class Meta:
        model = Client
        fields = ['id','name','address','cellphone','observation','photo','user','user_id']
        read_only_fields = ['id']

    def create(self, validated_data):
        user_id = validated_data.pop('user_id')
        user_found = get_object_or_404(User, id = user_id)
        
        client = Client.objects.create(**validated_data, user=user_found)

        return client

    def update(self, instance, validated_data):
        if validated_data:
            for key, value in validated_data.items():
                setattr(instance, key, value)
                instance.save()

        super().update(instance, validated_data)
        return instance