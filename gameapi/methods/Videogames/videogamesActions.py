from django.http import JsonResponse
from rest_framework.parsers import JSONParser

from gameapi.methods.Auth.user_authorization import validate_jwt

from gameapi.models import Videogame
from gameapi.serializers import VideogameSerializer

def videogames_actions(request):
    if request.method == 'POST': # Create new videogame
        data = JSONParser().parse(request)
        videogame = VideogameSerializer(data=data)

        if videogame.is_valid():
            videogame.save()
            return JsonResponse(videogame.data, status=201)
    
    elif request.method == 'GET': # Get all videogames
        # if validate_jwt(request) == True:
        videogames = Videogame.objects.all()
        serialized_videogames = VideogameSerializer(videogames, many=True)
        return JsonResponse(serialized_videogames.data, safe=False)
        # else:
        #     return JsonResponse({'message': 'Not authorized. User should be logged in.'}, status=401)