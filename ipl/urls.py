from django.urls import path
from . import views

urlpatterns = [
    path('', views.first, name='ipl-home'),
    path('api/first',views.match_per_season, name='ipl-season'),
    path('api/second',views.match_won_per_team, name='team-data'),
    path('api/third',views.extra_runs_team,name='extra-runs'),
    path('api/fourth',views.economical_bowler, name='economy'),
    path('api/fifth',views.sixes_hitters,name='sixes'),
    path('api/match/<int:id>', views.get_match, name='match-details'),
    path('api/Match',views.create_match,name='create-match'),
    path('api/Delivery',views.create_delivery,name='create_delivery'),
    path('api/delivery/<int:id>',views.get_delivery,name='delivery-details')
]
