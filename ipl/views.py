import json
from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from django.db.models import Count
from .models import Match
# Create your views here.

def match_per_season(request):
    '''api route here'''
    matches = Match.objects.values('season').annotate(matches=Count('season')).order_by('season')
    print(matches)
    season = list()
    match = list()
    for x in matches:
        season.append(x['season'])
        match.append(x['matches'])
    match_per_season = {
        'season':season,
        'matches':match
    }
    print(match_per_season)
    response = JsonResponse(match_per_season)
    return response


def first(request):
    '''route for first part'''
    return render(request,'ipl/first.html')


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

def second(request):
    return render(request,'ipl/second.html')