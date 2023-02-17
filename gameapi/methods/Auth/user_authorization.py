from project.constants import encrypt_key
import jwt

def get_jwt_params(request):
    encoded_jwt = request.headers.get('Authorization')
    decoded_jwt = jwt.decode(encoded_jwt, encrypt_key(), algorithms=['HS256'])

    if decoded_jwt['email'] and decoded_jwt['user']:
        return decoded_jwt
    else:
        return {'user': 'null', 'email': 'null'}