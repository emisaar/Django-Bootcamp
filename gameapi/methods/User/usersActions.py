from django.http import JsonResponse
from rest_framework.parsers import JSONParser

from gameapi.serializers import UserSerializer

def users_actions(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)

        user = UserSerializer(data=data)

        if user.is_valid():
            user.save()
            return JsonResponse(user.data, status=201)
        else:
            return JsonResponse(user.errors, status=400)