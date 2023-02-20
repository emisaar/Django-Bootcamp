from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from gameapi.methods.Auth.user_authorization import validate_jwt

from gameapi.models import User

from gameapi.serializers import UserSerializer

def users_actions(request):
    if request.method == 'POST': # Create a new user
        data = JSONParser().parse(request)

        user = UserSerializer(data=data)

        if user.is_valid():
            user.save()
            return JsonResponse(user.data, status=201)
        else:
            return JsonResponse(user.errors, status=400)
    elif request.method == 'GET': # Get all users (Only access when you are logged in)
        if validate_jwt(request) == True:
            users = User.objects.all()
            users_serializer = UserSerializer(users, many=True)
            return JsonResponse(users_serializer.data, safe=False)
        else:
            return JsonResponse({'message': 'Not authorized. User must be logged in.'}, status=401)