from django.urls import path
from . import views

urlpatterns = [
    path('', views.first, name='ipl-home'),
    path('api/first',views.match_per_season, name='ipl-season'),
    path('api/second',views.match_won_per_team, name='team-data'),
    path('api/third',views.extra_runs_team,name='extra-runs'),
    path('api/fourth',views.economical_bowler, name='economy'),
    path('api/match/<int:id>', views.match_get, name='match-details')
]
