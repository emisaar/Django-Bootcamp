from rest_framework.parsers import JSONParser
from django.http import JsonResponse

from gameapi.models import User
from gameapi.serializers import UserSerializer

from gameapi.variables.responses import user_not_found, user_deleted

def user_actions(request, pk):
    try:
        user_obj = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return JsonResponse(user_not_found, status=404)

    serialized_user = UserSerializer(user_obj)

    if request.method == 'GET': # Get user
        user_data = serialized_user.data

        data_dict = {'user': user_data}

        return JsonResponse(data_dict, status=200)
    
    elif request.method == 'PUT': # Update user
        data = JSONParser().parse(request)

        user_obj.name = data['name']
        user_obj.last_name = data['last_name']

        user_obj.save()

        return JsonResponse(serialized_user.data, status=200)

    elif request.method == 'DELETE': # Delete user
        user_obj.delete()
        return JsonResponse(user_deleted(), status=204)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)