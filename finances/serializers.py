from rest_framework import serializers
from .models import Finance
from users.models import User
from django.shortcuts import get_object_or_404


class FinanceSerializer(serializers.ModelSerializer):
    user_id = serializers.UUIDField(write_only=True)

    class Meta:
        model = Finance
        fields = ['id','user_id','description','type','value']
        read_only_fields = ['id']

    def create(self, validated_data):
        user_id = validated_data.pop('user_id')
        user_found = get_object_or_404(User, id = user_id)

        finance = Finance.objects.create(**validated_data, user=user_found)

        return finance

    def update(self, instance, validated_data):
        if validated_data:
            for key, value in validated_data.items():
                setattr(instance, key, value)
                instance.save()

        super().update(instance, validated_data)
        return instance