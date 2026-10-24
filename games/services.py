from django.db.models import Avg, Count

from .models import Rating, Review


def with_rating_stats(games):
    """Add .avg_rating and .num_ratings to every game in a Game queryset."""
    return games.annotate(
        avg_rating=Avg("ratings__score"),
        num_ratings=Count("ratings", distinct=True),
    )


def set_rating(user, game, score, review_text=""):
    """Create or update this user's rating for a game (and optional review).

    Raises ValueError if score is not a whole number from 1 to 5."""
    if isinstance(score, bool) or not isinstance(score, int) or not 1 <= score <= 5:
        raise ValueError("score must be a whole number from 1 to 5")

    rating, _ = Rating.objects.update_or_create(
        user=user, game=game, defaults={"score": score}
    )
    review_text = (review_text or "").strip()
    if review_text:
        Review.objects.update_or_create(
            user=user, game=game, defaults={"rating": rating, "body": review_text}
        )
    return rating


def get_user_rating(user, game):
    """The user's Rating for this game, or None (also None if logged out)."""
    if not user.is_authenticated:
        return None
    return Rating.objects.filter(user=user, game=game).first()


def recent_reviews(limit=10):
    """Newest reviews first, with user/game/rating preloaded for templates."""
    return Review.objects.select_related("user", "game", "rating")[:limit]