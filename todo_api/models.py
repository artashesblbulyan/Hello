from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.conf import settings


class User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    # posts_picture = models.ImageField(upload_to=user_post_directory_path)
    posts = models.TextField()
    # share = models.BooleanField(default=False)
    # amount_of_likes = models.IntegerField(default=0)
    # amount_of_dislikes = models.IntegerField(default=0)

    def __str__(self):
        return self.posts


class Drive(models.Model):
    CHOICES = (
        ("DR", 'driver'),
        ("PR", "passenger"),
    )

    Comment = models.CharField(max_length=180)
    Start = models.FloatField()
    End = models.FloatField()
    Status = models.CharField(choices=CHOICES, max_length=100)
    DateTimeStart = models.DateTimeField(auto_now=False, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.Comment