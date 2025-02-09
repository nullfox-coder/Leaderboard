from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'games', views.GameViewSet)
router.register(r'contestants', views.ContestantViewSet)
router.register(r'game-sessions', views.GameSessionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('leaderboard/global/', views.global_leaderboard, name='global-leaderboard'),
    path('leaderboard/game/<int:game_id>/', views.game_leaderboard, name='game-leaderboard'),
    path('game/popularity/', views.game_popularity, name='game-popularity'),
]