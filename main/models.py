from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(max_length=13, null=True, blank=True)
    bio = models.CharField(max_length=150, null=True, blank=True)
    avatar = models.ImageField(upload_to='user-avatar/', null=True, blank=True)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Banner(models.Model):
    img = models.ImageField(upload_to='banner_photos/')


class Info(models.Model):
    text = models.TextField()
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to="user_photos/")
    facebook = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)


class Contact(models.Model):
    text = models.TextField()
    email = models.CharField(max_length=50)
    number = models.CharField(max_length=13)
    address = models.CharField(max_length=200)


class Massage(models.Model):
    massage = models.CharField(max_length=255)
