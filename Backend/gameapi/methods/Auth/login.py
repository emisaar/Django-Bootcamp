from rest_framework.parsers import JSONParser
from django.http import JsonResponse

from gameapi.models import User
from gameapi.serializers import UserSerializer, SessionSerializer

import bcrypt
import jwt
from project.constants import encrypt_key

from gameapi.variables.responses import login_success, login_error, login_failed

from datetime import datetime

def login_method(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        email = data['email']
        password = data['password'].encode("utf-8")
        
        try:
            user_obj = User.objects.get(email=email)
        except User.DoesNotExist:
            return JsonResponse(login_error, status=405)

        user = UserSerializer(user_obj)
        print(user.data['password'].encode("utf-8"))
    
        if bcrypt.checkpw(password, user.data['password'].encode("utf-8")):
        # if password == user.data['password'].encode("utf-8"):
            now = datetime.now()
            payload = {
                'sign_in': str(now),
                'email': user.data['email'],
                'user': user.data['id']
            }
            encoded_jwt = jwt.encode(payload, encrypt_key(), algorithm='HS256'
            )
            print("User: "+user.data['email']+' logged at: '+str(now))
            sessionData = {'user': user.data['id'], 'jwt': encoded_jwt, 'sign_in': str(now), 'sign_out': 'null'}
            session = SessionSerializer(data=sessionData)
            if session.is_valid():
                session.save()
            return JsonResponse(session.data, status=200)
        return JsonResponse(login_error, status=405)

    else:
        return JsonResponse(login_error, status=405)