from django.http import JsonResponse
from rest_framework.parsers import JSONParser

from gameapi.models import Favorite, Videogame, User
from gameapi.serializers import FavoriteSerializer

from gameapi.methods.Auth import get_jwt_params

def favorites_actions(request):
    print(request)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        print("DATA: ", data)
        user = User.objects.get(pk=get_jwt_params(request)['user'])
        videogame = Videogame.objects.get(pk=data['resource_id'])

        favorite = Favorite(
            user=user,
            videogame=videogame,
        )

        favorite.save()
        serialized_favorite = FavoriteSerializer(favorite)
        return JsonResponse(serialized_favorite.data, status=201)
    elif request.method == 'GET':
        favourites = Favorite.objects.filter(user=get_jwt_params(request)['user'])
        favourites_list = []

        for favorite in favourites:
            fav_obj = {
                'id': favorite.id,
                'resource_name': favorite.videogame.title,
            }
            favourites_list.append(fav_obj)
        return JsonResponse(favourites_list, status=200, safe=False)
    elif request.method == 'DELETE':
        data = JSONParser().parse(request)
        print("DATA: ", data)
        favorite = Favorite.objects.get(pk=data['resource_id'])
        favorite.delete()
        return JsonResponse({'message': 'Favorite deleted'}, status=200)