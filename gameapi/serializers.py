from rest_framework import serializers

from .models import User

import bcrypt

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        managed = True
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

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
        