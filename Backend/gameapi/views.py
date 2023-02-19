from django.views.decorators.csrf import csrf_exempt

from gameapi.methods.Auth import (login_method, logout_method)
from gameapi.methods.Users import user_actions, users_actions

# Create your views here.

# Create new user or get all users
@csrf_exempt
def users_view(request):
    return users_actions(request=request)

# CRUD for user
@csrf_exempt
def user_view(request, pk):
    return user_actions(request=request, pk=pk)

# Login
@csrf_exempt
def login(request):
    return login_method(request=request)

# Logout
@csrf_exempt
def logout(request):
    return logout_method(request=request)
