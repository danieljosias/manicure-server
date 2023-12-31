from rest_framework import serializers
from .models import Admins
from users.serializers import UserSerializer
from users.models import Users


class AdminSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Admins
        fields = ['id', 'user']
        read_only_fields = ['id']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = Users.objects.create_user(**user_data)
        validated_data["user"] = user

        admin = Admins.objects.create(**validated_data)

        return admin
    
    def update(self, instance, validated_data):
        try:
            request_user = validated_data.pop('user')
        except KeyError:
            request_user = False    

        if request_user:
            for key, value in request_user.items():
                setattr(instance.user, key, value)
                instance.save()

        super().update(instance, validated_data)
        return instance
