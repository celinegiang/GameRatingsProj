import json
from pathlib import Path

from django.core.management.base import BaseCommand

from games.models import Game, Genre, Platform

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

        self.stdout.write(
            self.style.SUCCESS(
                f"Done. {Game.objects.count()} games, "
                f"{Genre.objects.count()} genres, {Platform.objects.count()} platforms."
            )
        )