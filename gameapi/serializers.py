from rest_framework import serializers

from .models import User, Session, Company, Genre, Videogame, Favorite, Review

import bcrypt

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        managed = True
        model = User
        fields = '__all__'
        # extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        bytePwd = validated_data['password'].encode('utf-8')
        
        mySalt = bcrypt.gensalt()
        hash = bcrypt.hashpw(bytePwd, mySalt)

        user = User(
            name = validated_data['name'],
            last_name = validated_data['last_name'],
            username = validated_data['username'],
            email = validated_data['email'],
            password = hash.decode('utf-8'),
        )
        user.save()
        return user
        
class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        managed = True
        model = Session
        fields = '__all__'

    def __str__(self):
        return self.jwt

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        managed = True
        model = Company
        fields = '__all__'

    def __str__(self):
        return self.name

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        managed = True
        model = Genre
        fields = '__all__'

    def __str__(self):
        return self.genre_name

class VideogameSerializer(serializers.ModelSerializer):
    class Meta:
        managed = True
        model = Videogame
        fields = '__all__'

    def __str__(self):
        return self.title
    
class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        managed = True
        model = Favorite
        fields = '__all__'

    def __str__(self):
        return self.title
    
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        managed = True
        model = Review
        fields = '__all__'

    def __str__(self):
        return self.title