from django.shortcuts import render

# Create your views here.
from .models import Game


def game_list(request):
    q = request.GET.get("q", "").strip()
    games = Game.objects.prefetch_related("genres", "platforms")
    if q:
        games = games.filter(title__icontains=q)
    return render(request, "games/game_list.html", {"games": games, "q": q})