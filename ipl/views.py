import json
from django.core import serializers
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.http import HttpResponse,JsonResponse
from django.db.models import Count,Sum,FloatField, F, When, Case
from django.db.models.functions import Cast
from django.forms import ModelForm
from .models import Match,Delivery
# Create your views here.

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

@cache_page(CACHE_TTL)
def match_per_season(request):
    '''api route here'''
    matches = Match.objects.values('season').annotate(matches=Count('season')).order_by('season')
    season = list()
    match = list()
    for x in matches:
        season.append(x['season'])
        match.append(x['matches'])
    match_per_season = {
        'season':season,
        'matches':match
    }
    response = JsonResponse(match_per_season)
    return response

@cache_page(CACHE_TTL)
def first(request):
    '''route for first part'''
    return render(request,'ipl/first.html')

@cache_page(CACHE_TTL)
def match_won_per_team(request):
    '''api route for second part'''

    teams = Match.objects.values('winner','season').annotate(total_win=Count('winner')).order_by('season','winner')
    years=list(Match.objects.values_list('season', flat=True).distinct().order_by('season'))
    team_list = set()
    team_win_details = dict()
    for team in teams:
        if team['winner'] != None:
            team_list.add(team['winner'])
    team_list = list(team_list)
    team_list.sort()
    for team in team_list:
        team_win_details[team] = [0]*len(years)
    for row in teams:
        if row['winner'] != None:
            winner = row['winner']
        total_win = row['total_win']
        year = row['season']
        team_win_details[winner][years.index(year)] = total_win
    teamwons = {"years":years}
    list_ =[]
    for team,win_details in team_win_details.items():
        list_.append({
            "name":team,
            "data":win_details
        })
    teamwons["seriesdata"]=list_
    print(teamwons)
    return  JsonResponse(teamwons)

@cache_page(CACHE_TTL)
def extra_runs_team(request):
    '''api route for third part'''

    extra_runs = Delivery.objects.filter(match__season=2016).values('bowling_team').annotate(extras=Sum('extra_runs')).order_by('extras')
    teams = list()
    extra = list()
    for runs in extra_runs:
        teams.append(runs['bowling_team'])
        extra.append(runs['extras'])
    extra_runs_per_team = {
        'teams':teams,
        'extras':extra
    }
    return JsonResponse(extra_runs_per_team)

@cache_page(CACHE_TTL)
def economical_bowler(request):
    '''api for fourth question'''

    economy_details = economy_helper()
    bowlers = list()
    economy = list()
    for data in economy_details:
        bowlers.append(data['bowler'])
        economy.append(data['economy'])
    bowler_economy = {
        'bowlers':bowlers,
        'economy':economy
    }
    return JsonResponse(bowler_economy)


class MatchForm(ModelForm):
    class Meta:
        model = Match
        fields = '__all__'

def match_get(request,id):

    match = Match.objects.get(pk=id)
    form = MatchForm(instance=match)
    return render(request,'ipl/form.html',{'form':form})

'''helper function for economical_bowler'''
def economy_helper():
    economy_query_set = Delivery.objects.filter(match__season=2015,is_super_over=0).values('bowler').annotate(runs=(Sum('total_runs')-Sum('bye_runs')-Sum('legbye_runs'))*6.0).annotate(balls=(Count('ball')-Count(Case(When(noball_runs__gt=0, then=1)))-Count(Case(When(wide_runs__gt=0, then=1))))).annotate(economy= Cast(F('runs')/F('balls'), FloatField())).order_by('economy')[:10]

    return economy_query_set
