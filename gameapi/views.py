from django.views.decorators.csrf import csrf_exempt

from gameapi.methods.Auth import (login_method, logout_method)
from gameapi.methods.Users import user_actions, users_actions
from gameapi.methods.Companies import company_actions, companies_actions
from gameapi.methods.Genres import genres_actions
from gameapi.methods.Videogames import videogames_actions, videogame_actions
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

# Create new company or Get all companies
@csrf_exempt
def companies_view(request):
    return companies_actions(request=request)

@csrf_exempt
def company_view(request, pk):
    return company_actions(request=request, pk=pk)

@csrf_exempt
def genres_view(request):
    return genres_actions(request=request)

@csrf_exempt
def videogames_view(request):
    return videogames_actions(request=request)

@csrf_exempt
def videogame_view(request, pk):
    return videogame_actions(request=request, pk=pk)