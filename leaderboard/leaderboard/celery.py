import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'leaderboard.settings')

app = Celery('leaderboard')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# Schedule the popularity calculation task
app.conf.beat_schedule = {
    'calculate-game-popularity': {
        'task': 'game.tasks.calculate_game_popularity',
        'schedule': 300.0,  # 5 minutes
    },
}
