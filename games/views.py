from django.contrib.auth.views import redirect_to_login
from django.shortcuts import get_object_or_404, redirect, render

from . import services
from .forms import RatingForm
from .models import Game, Genre, Platform
from .models import Game, Genre, Platform

def home(request):
    """Homepage: the most recent reviews."""
    return render(
        request, "home.html", {"recent_reviews": services.recent_reviews(10)}
    )

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

    games = services.with_rating_stats(games)

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

def game_detail(request, pk):
    game = get_object_or_404(
        Game.objects.prefetch_related("genres", "platforms"), pk=pk
    )
    user_rating = services.get_user_rating(request.user, game)

    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect_to_login(request.get_full_path())
        form = RatingForm(request.POST)
        if form.is_valid():
            services.set_rating(
                request.user,
                game,
                form.cleaned_data["score"],
                form.cleaned_data["body"],
            )
            return redirect("game_detail", pk=game.pk)
    else:
        initial = {}
        if user_rating:
            initial["score"] = user_rating.score
            if hasattr(user_rating, "review"):
                initial["body"] = user_rating.review.body
        form = RatingForm(initial=initial)

    return render(
        request,
        "games/game_detail.html",
        {
            "game": game,
            "form": form,
            "user_rating": user_rating,
            "avg_rating": game.average_rating(),
            "num_ratings": game.ratings.count(),
            "reviews": game.reviews.select_related("user", "rating"),
        },
    )