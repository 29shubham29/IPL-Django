from rest_framework import serializers
from ipl.models import Match,Delivery

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields =  ['season', 'city', 'date', 'team1', 'team2','toss_winner','toss_decision', 'result', 'dl_applied',
                 'winner', 'win_by_runs', 'win_by_wickets', 'player_of_match','venue', 'umpire1', 'umpire2', 'umpire3']

class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = ['match_id', 'inning', 'batting_team', 'bowling_team','over', 'ball', 'batsman', 'non_striker','bowler', 'is_super_over', 'wide_runs', 'bye_runs','legbye_runs', 'noball_runs', 'penalty_runs','batsman_runs','extra_runs', 'total_runs', 'player_dismissed', 'dismissal_kind','fielder']