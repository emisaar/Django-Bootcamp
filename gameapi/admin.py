from django.contrib import admin

from gameapi.models import User, Session, Company, Genre, Videogame, Favorite

# Register your models here.
admin.site.register(User)
admin.site.register(Session)
admin.site.register(Company)
admin.site.register(Genre)
admin.site.register(Videogame)
admin.site.register(Favorite)