from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from django.db.models import Count, Max
from .models import Game, GameSession, GamePopularity

@shared_task
def calculate_game_popularity():
    yesterday = timezone.now() - timedelta(days=1)
    
    # Calculate maximums
    max_daily_players = max(
        GameSession.objects.filter(start_time__gte=yesterday)
        .values('game')
        .annotate(count=Count('contestant', distinct=True))
        .aggregate(Max('count'))['count__max'] or 1,
        1
    )
    
    max_concurrent_players = max(
        GameSession.objects.filter(is_active=True)
        .values('game')
        .annotate(count=Count('id'))
        .aggregate(Max('count'))['count__max'] or 1,
        1
    )
    
    max_upvotes = max(
        Game.objects.all()
        .aggregate(Max('upvotes'))['upvotes__max'] or 1,
        1
    )
    
    yesterday_sessions = GameSession.objects.filter(
        start_time__gte=yesterday,
        end_time__isnull=False
    )
    
    max_session_length = max(
        yesterday_sessions.values('game')
        .annotate(length=Max('end_time') - Max('start_time'))
        .aggregate(Max('length'))['length__max'].total_seconds() if yesterday_sessions else 1,
        1
    )
    
    max_daily_sessions = max(
        yesterday_sessions.values('game')
        .annotate(count=Count('id'))
        .aggregate(Max('count'))['count__max'] or 1,
        1
    )

    print(max_daily_players, max_concurrent_players, max_upvotes, max_session_length, max_daily_sessions)
    
    # Calculate popularity for each game
    for game in Game.objects.all():
        w1 = GameSession.objects.filter(
            game=game,
            start_time__gte=yesterday
        ).values('contestant').distinct().count()
        
        w2 = GameSession.objects.filter(
            game=game,
            is_active=True
        ).count()
        
        w3 = game.upvotes
        
        game_yesterday_sessions = yesterday_sessions.filter(game=game)
        w4 = max(
            [(s.end_time - s.start_time).total_seconds() 
             for s in game_yesterday_sessions],
            default=0
        )
        w5 = game_yesterday_sessions.count()
        
        popularity_score = (
            0.3 * (w1/max_daily_players) +
            0.2 * (w2/max_concurrent_players) +
            0.25 * (w3/max_upvotes) +
            0.15 * (w4/max_session_length) +
            0.1 * (w5/max_daily_sessions)
        )
        
        GamePopularity.objects.update_or_create(
            game=game,
            defaults={'popularity_score': popularity_score}
        )