from rest_framework import viewsets, status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from django.utils import timezone
from django.db.models import Max
from datetime import timedelta
from .models import Game, Contestant, GameSession, GamePopularity
from .serializers import  GameSerializer, ContestantSerializer, GameSessionSerializer, LeaderboardEntrySerializer, GamePopularitySerializer

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    @action(detail=True, methods=['post'])
    def upvote(self, request, pk=None):
        game = self.get_object()
        game.upvotes += 1
        game.save()
        return Response({'message': 'Game upvoted successfully'})

class ContestantViewSet(viewsets.ModelViewSet):
    queryset = Contestant.objects.all()
    serializer_class = ContestantSerializer

class GameSessionViewSet(viewsets.ModelViewSet):
    queryset = GameSession.objects.all()
    serializer_class = GameSessionSerializer

    @action(detail=True, methods=['put'])
    def end(self, request, pk=None):
        session = self.get_object()
        session.end_time = timezone.now()
        session.is_active = False
        session.save()
        return Response({'message': 'Session ended successfully'})

    @action(detail=True, methods=['put'])
    def update_score(self, request, pk=None):
        session = self.get_object()
        score = request.data.get('score')
        if score is not None:
            session.score = float(score)
            session.save()
            return Response({'message': 'Score updated successfully'})
        return Response({'error': 'Score is required'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def global_leaderboard(request):
    sessions = GameSession.objects.select_related('contestant', 'game').order_by('-score')[:10]
    data = [
        {
            'contestant_name': session.contestant.name,
            'game_name': session.game.name,
            'score': session.score
        }
        for session in sessions
    ]
    serializer = LeaderboardEntrySerializer(data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def game_leaderboard(request, game_id):
    sessions = GameSession.objects.filter(game_id=game_id).select_related('contestant').order_by('-score')[:10]
    data = [
        {
            'contestant_name': session.contestant.name,
            'score': session.score
        }
        for session in sessions
    ]
    serializer = LeaderboardEntrySerializer(data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def game_popularity(request):
    popularities = GamePopularity.objects.all()
    serializer = GamePopularitySerializer(popularities, many=True)
    return Response(serializer.data)