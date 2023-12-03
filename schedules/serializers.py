from rest_framework import serializers
from .models import Schedules
from users.models import Users
from django.shortcuts import get_object_or_404
from users.serializers import UserSerializer

class ScheduleSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.UUIDField(write_only=True)
    class Meta:
        model = Schedules
        fields = ['id','user','user_id','name','cellphone','date','hour','service','price']
        read_only_fields = ['id']

    def create(self, validated_data):
        user_id = validated_data.pop('user_id')
        user_found = get_object_or_404(Users, id = user_id)

        schedule = Schedules.objects.create(**validated_data, user=user_found)

        return schedule

    def update(self, instance, validated_data):
        if validated_data:
            for key, value in validated_data.items():
                setattr(instance, key, value)
                instance.save()

        super().update(instance, validated_data)
        return instance