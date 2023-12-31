from rest_framework import serializers
from .models import Finances
from users.models import Users
from users.serializers import UserSerializer
from django.shortcuts import get_object_or_404


class FinanceSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.UUIDField(write_only=True)

    class Meta:
        model = Finances
        fields = ['id','user','user_id','description','type','value']
        read_only_fields = ['id']

    def create(self, validated_data):
        user_id = validated_data.pop('user_id')
        user_found = get_object_or_404(Users, id = user_id)

        finance = Finances.objects.create(**validated_data, user=user_found)

        return finance

   