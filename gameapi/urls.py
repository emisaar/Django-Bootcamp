from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('users/', views.users_view, name='users_actions'),
    path('user/<int:pk>/', views.user_view, name='user_actions'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('companies/', views.companies_view, name='companies_actions'),
    path('company/<int:pk>', views.company_view, name='company_actions'),
    path('genres/', views.genres_view, name='genres_actions'),
    path('videogames/', views.videogames_view, name='videogames_actions'),
    path('videogame/<int:pk>', views.videogame_view, name='videogame_actions')
]