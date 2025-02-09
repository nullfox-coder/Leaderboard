from rest_framework import serializers
from .models import Game, Contestant, GameSession, GamePopularity

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'name', 'upvotes', 'created_at']

class ContestantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contestant
        fields = ['id', 'name', 'email', 'created_at']

class GameSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameSession
        fields = ['id', 'game', 'contestant', 'score', 'start_time', 'end_time', 'is_active']

class LeaderboardEntrySerializer(serializers.Serializer):
    contestant_name = serializers.CharField()
    game_name = serializers.CharField(required=False)
    score = serializers.FloatField()

class GamePopularitySerializer(serializers.ModelSerializer):
    game_name = serializers.CharField(source='game.name')

    class Meta:
        model = GamePopularity
        fields = ['game_name', 'popularity_score', 'calculation_time']
