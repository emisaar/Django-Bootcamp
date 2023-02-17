from rest_framework.parsers import JSONParser
from django.http import JsonResponse

from models import User

from serializers import UserSerializer

from gameapi.variables.responses import login_success, login_error

def login_method(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        email = data['email']
        password = data['password'].encode('utf-8')
        
        try:
            user_obj = User.objects.get(email=email)
        except User.DoesNotExist:
            return JsonResponse(login_error, status=401)

        user = UserSerializer(user_obj)