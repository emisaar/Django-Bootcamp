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

    def __str__(self):
        return self.jwt

class Company(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=255)
    country = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name_plural = "Companies"

class Genre(models.Model):
    id = models.AutoField(primary_key=True)
    genre_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.genre_name

class Videogame(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/videogames')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

# class VideogameImage(models.Model):
#     id = models.AutoField(primary_key=True)
#     videogame = models.ForeignKey(Videogame, on_delete=models.CASCADE)

#     url = models.CharField(max_length=255)
#     uploaded_at = models.DateTimeField(default=timezone.now)

    # def __str__(self):
    #     return {
    #         self.image_name
    #     }

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    videogame = models.ForeignKey(Videogame, on_delete=models.CASCADE)
    review = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

class Favorite(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    videogame = models.ForeignKey(Videogame, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

