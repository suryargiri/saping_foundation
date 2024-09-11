from django.urls import path
from .views import index, team_nepal

urlpatterns = [
    path('', index, name='index'),
    path('team_nepal/', team_nepal, name='team_nepal'),
]
