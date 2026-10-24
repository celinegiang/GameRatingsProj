from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import Avg
from django.utils import timezone

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Platform(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    release_year = models.PositiveIntegerField(null=True, blank=True)
    developer = models.CharField(max_length=200, blank=True)
    cover_url = models.URLField(blank=True)
    genres = models.ManyToManyField(Genre, related_name="games", blank=True)
    platforms = models.ManyToManyField(Platform, related_name="games", blank=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title

    def average_rating(self):
        return self.ratings.aggregate(avg=Avg("score"))["avg"]

class Rating(models.Model):
       """One 1-5 score per user per game (rating again updates it)."""

       user = models.ForeignKey(
           settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="ratings"
       )
       game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="ratings")
       score = models.PositiveSmallIntegerField(
           validators=[MinValueValidator(1), MaxValueValidator(5)]
       )
       created_at = models.DateTimeField(auto_now_add=True)

       class Meta:
           constraints = [
               models.UniqueConstraint(
                   fields=["user", "game"], name="one_rating_per_user_per_game"
               )
           ]

       def __str__(self):
           return f"{self.user} rated {self.game}: {self.score}/5"


class Review(models.Model):
       """Optional written review, usually attached to the user's Rating."""

       user = models.ForeignKey(
           settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reviews"
       )
       game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="reviews")
       rating = models.OneToOneField(
           Rating,
           null=True,
           blank=True,
           on_delete=models.SET_NULL,
           related_name="review",
       )
       body = models.TextField()
       created_at = models.DateTimeField(default=timezone.now)

       class Meta:
           ordering = ["-created_at"]  # newest first
           constraints = [
               models.UniqueConstraint(
                   fields=["user", "game"], name="one_review_per_user_per_game"
               )
           ]

       def __str__(self):
           return f"{self.user} on {self.game}"