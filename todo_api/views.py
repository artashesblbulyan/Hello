import os
from pathlib import Path

from django.shortcuts import get_object_or_404, redirect
from django_rest.http import status
from rest_framework import generics, mixins
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView

from todo_api.models import Drive
from todo_api.serializers import RegisterSerializer, UserUpdateSerializer, DriveSerializer, DriveUpdateSerializer


# class RegisterView(CreateAPIView):
#     serializer_class = RegisterSerializer
#     template_name = 'rest_framework/registration.html'

class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [IsAuthenticated]


class HomeView(generics.RetrieveUpdateAPIView):
    serializer_class = UserUpdateSerializer
    lookup_field = 'username'
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return User.objects.filter(username=self.request.user)


class DriveView(generics.ListAPIView):
    serializer_class = DriveSerializer
    lookup_field = 'username'
    permission_classes = [IsAdminUser]
    template_name = "api_index.html"

    def get_queryset(self):
        username = self.kwargs['username']
        return Drive.objects.filter(user__username=username)
        # return Drive.objects.filter(user=self.request.user)

    # def filter_queryset(self,quergetiset):


class DriveUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = DriveUpdateSerializer
    lookup_field = 'id'
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        print(self.kwargs)
        username = self.kwargs['username']
        return Drive.objects.filter(user__username=username)