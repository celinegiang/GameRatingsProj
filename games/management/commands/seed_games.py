import json
from pathlib import Path
from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone
from django.contrib.auth import get_user_model

from games.models import Game, Genre, Platform, Rating, Review

# games/management/commands/seed_games.py -> parents[2] is the games/ folder
DATA_FILE = Path(__file__).resolve().parents[2] / "data" / "games.json"


class Command(BaseCommand):
    help = "Load the shared game catalog from games/data/games.json. Safe to run repeatedly."

    def handle(self, *args, **options):
        items = json.loads(DATA_FILE.read_text(encoding="utf-8"))

        for item in items:
            game, _ = Game.objects.update_or_create(
                title=item["title"],
                defaults={
                    "developer": item.get("developer", ""),
                    "release_year": item.get("release_year"),
                    "description": item.get("description", ""),
                    "cover_url": item.get("cover_url", ""),
                },
            )
            game.genres.set(
                [Genre.objects.get_or_create(name=n)[0] for n in item.get("genres", [])]
            )
            game.platforms.set(
                [Platform.objects.get_or_create(name=n)[0] for n in item.get("platforms", [])]
            )

        self.load_demo_reviews()

        self.stdout.write(
            self.style.SUCCESS(
                f"Done. {Game.objects.count()} games, "
                f"{Genre.objects.count()} genres, {Platform.objects.count()} platforms."
            )
        )

    def load_demo_reviews(self):
        """Demo users and reviews so the homepage isn't empty. Safe to rerun."""
        User = get_user_model()
        data = json.loads(
            (DATA_FILE.parent / "demo_reviews.json").read_text(encoding="utf-8")
        )

        for username in data["users"]:
            if not User.objects.filter(username=username).exists():
                user = User(username=username)
                user.set_unusable_password()  # demo users can't log in
                user.save()

        now = timezone.now()
        for item in data["reviews"]:
            user = User.objects.get(username=item["user"])
            game = Game.objects.get(title=item["game"])
            rating, _ = Rating.objects.update_or_create(
                user=user, game=game, defaults={"score": item["score"]}
            )
            
            # update the text if you edited the JSON; only set the date when first created
            Review.objects.update_or_create(
                user=user,
                game=game,
                defaults={"rating": rating, "body": item["body"]},
                create_defaults={
                    "rating": rating,
                    "body": item["body"],
                    "created_at": now - timedelta(days=item["days_ago"]),
                },
            )