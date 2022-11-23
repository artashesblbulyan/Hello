
from django import forms
from rest_framework import serializers
from .models import Drive
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class DriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drive
        fields = ["id", "Comment", "Start", "End", 'Status', "DateTimeStart", "updated", "user"]


class DriveUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drive
        fields = ["id", "Comment", "Start", "End", 'Status', "DateTimeStart", "updated", "user"]

    def update(self, instance, validated_data):
        instance.Comment = validated_data.get('Comment', instance.Comment),
        instance.Start = validated_data.get('Start', instance.Start),
        instance.End = validated_data.get('End', instance.End),
        instance.Status = validated_data.get('Status', instance.Status),
        instance.DateTimeStart = validated_data.get('DateTimeStart', instance.DateTimeStart),
        instance.save()

        return instance


# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#
#     @classmethod
#     def get_token(cls, user):
#         token = super(MyTokenObtainPairSerializer, cls).get_token(user)
#
#         # Add custom claims
#         token['username'] = user.username
#         return token


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def update(self, instance, validated_data):
        user = User.objects.get(username=instance)
        print(validated_data)
        user.username = validated_data["username"]
        user.email = validated_data['email']
        user.first_name = validated_data['first_name']
        user.last_name = validated_data['last_name']
        # user.set_password(validated_data['password'])
        # print(user)
        user.save()


        return user


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user