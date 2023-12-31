from rest_framework import serializers
from .models import Clients
from users.models import Users
from users.serializers import UserSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

class ClientSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.UUIDField(write_only=True)
    class Meta:
        model = Clients
        fields = ['id','name','address','cellphone','observation','user','user_id']
        read_only_fields = ['id']   

    def create(self, validated_data):
        user_id = validated_data.pop('user_id')
        user_found = get_object_or_404(Users, id = user_id)
        
        client = Clients.objects.create(**validated_data, user=user_found)

        return client
