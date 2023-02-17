from django.views.decorators.csrf import csrf_exempt

from gameapi.methods.Auth import (login_method, logout_method)
from gameapi.methods.User import users_actions

# Create your views here.
@csrf_exempt
def register(request):
    return users_actions(request=request)

@csrf_exempt
def login(request):
    return login_method(request=request)

@csrf_exempt
def logout(request):
    return logout_method(request=request)