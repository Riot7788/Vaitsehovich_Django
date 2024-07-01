from django.contrib.auth.models import User
# from booking_app.models import User
from booking_app.models import Hotel_owner
from booking_app.models import Hobby
from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(required=False, max_length=30)
    first_name = serializers.CharField(required=False, max_length=30)
    last_name = serializers.CharField(required=False, max_length=30)
    email = serializers.EmailField(required=False)

    def create(self, validated_data):
        return User.objects.create_user()

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)

        instance.save()
        return instance
# class UserModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ["username", "first_name", "last_name", "email","is_superuser",'is_staff']


class OwnerSerializer(serializers.Serializer):
    username = serializers.CharField(required=False, max_length=30)
    first_name = serializers.CharField(required=False, max_length=30)
    last_name = serializers.CharField(required=False, max_length=30)
    email = serializers.EmailField(required=False)

    def create(self, validated_data):
        return Hotel_owner.objects.create_user()

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)

        instance.save()
        return instance


class HobbySerializer(serializers.Serializer):
    name = serializers.CharField(required=False, max_length=50)

    def create(self, validated_data):
        return Hobby.objects.hobby()

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance