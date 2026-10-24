from django.contrib import admin

# Register your models here.
from .models import Game, Genre, Platform, Rating, Review

admin.site.register(Genre)
admin.site.register(Platform)
admin.site.register(Game)
admin.site.register(Rating)
admin.site.register(Review)