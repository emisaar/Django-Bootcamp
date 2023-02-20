from project.constants import encrypt_key
import jwt

from gameapi.models import Session
from django.db.models import Q

def validate_jwt(request):
    encoded_jwt = request.headers.get('Authorization')
    decoded_jwt = jwt.decode(encoded_jwt, encrypt_key(), algorithms=['HS256'])

    if decoded_jwt['email'] and decoded_jwt['user']:
        session_objs = Session.objects.filter(Q(user=decoded_jwt['user']) & Q(jwt=encoded_jwt)).values()
        print("Session: "+str(session_objs[0]['id'])+" is valid")
        print(session_objs)
        if session_objs[0]['sign_out'] == 'null':
            return True
        else:
            return False

def get_jwt_params(request):
    encoded_jwt = request.headers.get('Authorization')
    decoded_jwt = jwt.decode(encoded_jwt, encrypt_key(), algorithms=['HS256'])

    if decoded_jwt['email'] and decoded_jwt['user']:
        return decoded_jwt
    else:
        return {'user': 'null', 'email': 'null'}