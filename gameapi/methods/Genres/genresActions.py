from django.http import JsonResponse
from rest_framework.parsers import JSONParser

from gameapi.models import Genre
from gameapi.serializers import GenreSerializer

def genres_actions(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        genre = GenreSerializer(data=data)

        if genre.is_valid():
            genre.save()
            return JsonResponse(genre.data, status=201)
    elif request.method == 'GET':
        genres = Genre.objects.all()
        serialized_genres = GenreSerializer(genres, many=True)
        return JsonResponse(serialized_genres.data, safe=False)