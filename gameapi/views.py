from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from gameapi.methods.User import users_action

# Create your views here.
@csrf_exempt
def register(request):
    return users_action(request=request)