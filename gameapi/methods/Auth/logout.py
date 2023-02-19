from django.http import JsonResponse
from gameapi.models import User, Session

from gameapi.variables.responses import logout_success, not_allowed

from .user_authorization import get_jwt_params

from datetime import datetime
from django.db.models import Q

def logout_method(request):
    if request.method == 'POST' or request.method == 'GET':
        encoded_jwt = request.headers.get('Authorization')
        

        decoded_jwt = get_jwt_params(request)
        session_objs = Session.objects.filter(Q(user=decoded_jwt['user']) & Q(jwt=encoded_jwt))

        for session in session_objs:
            session.sign_out = str(datetime.now())
            session.save()
            return JsonResponse(logout_success(), status=201)

    else:
        return JsonResponse(logout_success(), status=405)