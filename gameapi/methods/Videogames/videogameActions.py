from django.http import JsonResponse
from rest_framework.parsers import JSONParser

from gameapi.models import User, Videogame, Company, Genre, Review
from gameapi.serializers import VideogameSerializer, ReviewSerializer

from gameapi.variables.responses import not_found

def videogame_actions(request, pk):
    print('pk: ', pk)
    try:
        videogame = Videogame.objects.get(pk=pk)
    except Videogame.DoesNotExist:
        return JsonResponse(not_found(), status=404)
    
    serialized_videogame = VideogameSerializer(videogame)

    if request.method == 'GET':
        videogame_data = serialized_videogame.data
        videogame_title = videogame_data['title']
        company_name = Company.objects.get(pk=videogame_data['company']).company_name
        genre_name = Genre.objects.get(pk=videogame_data['genre']).genre_name
        reviews = Review.objects.filter(videogame=pk)
        serialized_reviews = ReviewSerializer(reviews, many=True)

        reviews_data = []
        for review in serialized_reviews.data:
            user_username = User.objects.get(pk=review['user']).username
            data = {
                'id': review['id'],
                'review': review['review'],
                'created_at': review['created_at'],
                'user': user_username,
            }
            reviews_data.append(data)

        data_dict = {
            'id': videogame_data['id'],
            'title': videogame_data['title'],
            'company': company_name,
            'genre': genre_name,
            'created_at': videogame_data['created_at'],
            'reviews': reviews_data
        }
        return JsonResponse(data_dict, status=200)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        videogame.title = data['title']
        videogame.save()
        return JsonResponse(serialized_videogame.data, status=200)

    elif request.method == 'DELETE':
        videogame.delete()
        return JsonResponse(not_found(), status=204)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)