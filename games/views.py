from django.shortcuts import render

from .models import Game, Genre, Platform


def game_list(request):
    q = request.GET.get("q", "").strip()
    genre = request.GET.get("genre", "").strip()
    platform = request.GET.get("platform", "").strip()
    year = request.GET.get("year", "").strip()

    games = Game.objects.prefetch_related("genres", "platforms")
    if q:
        games = games.filter(title__icontains=q)
    if genre:
        games = games.filter(genres__name=genre)
    if platform:
        games = games.filter(platforms__name=platform)
    if year.isdigit():
        games = games.filter(release_year=int(year))
    else:
        year = ""  # ignore junk like ?year=abc

    years = (
        Game.objects.exclude(release_year=None)
        .order_by("-release_year")
        .values_list("release_year", flat=True)
        .distinct()
    )

    context = {
        "games": games,
        "genres": Genre.objects.all(),
        "platforms": Platform.objects.all(),
        "years": years,
        "q": q,
        "genre": genre,
        "platform": platform,
        "year": year,
    }
    return render(request, "games/game_list.html", context)