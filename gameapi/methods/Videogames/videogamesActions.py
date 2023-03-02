from django.http import JsonResponse
from rest_framework.parsers import JSONParser

from gameapi.methods.Auth.user_authorization import validate_jwt

from gameapi.models import Videogame, Company, Genre
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
        videogames_objs = Videogame.objects.all()
        serialized_videogames = VideogameSerializer(videogames_objs, many=True)
        
        data_dict = []

        for videogame in serialized_videogames.data:
            company_name = Company.objects.get(pk=videogame['company']).company_name
            genre_name = Genre.objects.get(pk=videogame['genre']).genre_name
            data = {
                'id': videogame['id'],
                'title': videogame['title'],
                'company': company_name,
                'image': videogame['image'],
                'genre': genre_name,
                'created_at': videogame['created_at']    
            }
            data_dict.append(data)

        return JsonResponse(data_dict, safe=False, status=200)
        # else:
        #     return JsonResponse({'message': 'Not authorized. User should be logged in.'}, status=401)