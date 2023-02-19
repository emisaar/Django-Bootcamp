from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username

class Session(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    jwt = models.CharField(max_length=500)
    sign_in = models.CharField(max_length=120)
    sign_out = models.CharField(max_length=120)

class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)

class Game(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    image = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    review = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

class Favorite(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

