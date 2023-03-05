from django.http import JsonResponse
from rest_framework.parsers import JSONParser

from gameapi.methods.Auth.user_authorization import validate_jwt

from gameapi.models import Videogame, Review
from gameapi.serializers import ReviewSerializer

def reviews_actions(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        review = ReviewSerializer(data=data)
        if review.is_valid():
            review.save()
            return JsonResponse(review.data, status=201)
        
    elif request.method == 'GET':
        # if validate_jwt(request) == True:
        reviews_objs = Review.objects.all()
        serialized_reviews = ReviewSerializer(reviews_objs, many=True)
        return JsonResponse(serialized_reviews.data, safe=False, status=200)
        # else:
        #     return JsonResponse({'message': 'Not authorized. User should be logged in.'}, status=401)