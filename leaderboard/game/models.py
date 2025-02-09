from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator

class Game(models.Model):
    name = models.CharField(max_length=100, unique=True)
    upvotes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Contestant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class GameSession(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='sessions')
    contestant = models.ForeignKey(Contestant, on_delete=models.CASCADE, related_name='sessions')
    score = models.FloatField(default=0, validators=[MinValueValidator(0)])
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.contestant.name} - {self.game.name}"

class GamePopularity(models.Model):
    game = models.OneToOneField(Game, on_delete=models.CASCADE, related_name='popularity')
    popularity_score = models.FloatField(default=0)
    calculation_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.game.name} - {self.popularity_score}"
