import json
from django.core import serializers
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.http import HttpResponse,JsonResponse,Http404
from django.db.models import Count,Sum,FloatField, F, When, Case
from django.db.models.functions import Cast
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
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

def first(request):
    '''route for first part'''
    return render(request,'ipl/first.html')

@cache_page(CACHE_TTL)
def match_won_per_team(request):
    '''api route for second part'''

    teams = Match.objects.values('winner','season').annotate(total_win=Count('winner')).order_by('season','winner')
    years = list(Match.objects.values_list('season', flat=True).distinct().order_by('season'))
    team_win_details = teams_helper(teams,years)
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

def sixes_hitters(request):
    '''api for fifth question'''
    batsman_details = Delivery.objects.filter(match__season=2016).values('batsman').annotate(sixes = Count(Case(When(batsman_runs=6, then=1)))).order_by('-sixes')[:10]
    name = list()
    sixes = list()
    for batsman in batsman_details:
        name.append(batsman['batsman'])
        sixes.append(batsman['sixes'])
    six_details = {
        'batsman': name,
        'sixes': sixes
    }
    return JsonResponse(six_details)

class MatchForm(ModelForm):
    class Meta:
        model = Match
        fields = '__all__'

class DeliveryForm(ModelForm):
    class Meta:
        model = Delivery
        fields = '__all__'

# def create_delivery(request):
#     form = DeliveryForm()
#     return render(request,'ipl/delivery.html',{'form':form})

#apis for crud operations
'''api for matches'''
@csrf_exempt
def get_match(request,id):
    if request.method == 'GET':
        try:
            match = Match.objects.values().get(pk=id)
        except Match.DoesNotExist:
            raise Http404
    return JsonResponse(match)

def save_data(data, key):
    try:
        return data[key]
    except:
        raise KeyError(f'Missing argument :: {key}')

'''api for match creation'''
@csrf_exempt
def create_match(request):
    if request.method == 'POST':
        if request.body:
            data = json.loads(request.body.decode('utf-8'))
        else:
            return JsonResponse({'error':'No data'})
        try:
            match = Match()
            match.season         = save_data(data,'season')
            match.city           = save_data(data,'city')
            match.date           = save_data(data,'date')
            match.team1          = save_data(data,'team1')
            match.team2          = save_data(data,'team2')
            match.toss_winner    = save_data(data,'toss_winner')
            match.toss_decision  = save_data(data,'toss_decision')
            match.result         = save_data(data,'result')
            match.dl_applied     = save_data(data,'dl_applied')
            match.winner         = save_data(data,'winner')
            match.win_by_runs    = save_data(data,'win_by_runs')
            match.player_of_match= save_data(data,'player_of_match')
            match.venue          = save_data(data,'venue')
            match.umpire1        = save_data(data,'umpire1')
            match.umpire2        = save_data(data,'umpire2')
            match.umpire3        = save_data(data,'umpire3')
            match.save()
        except KeyError as error:
            result = {'error':str(error)}
            return JsonResponse(result)
        except Exception as error:
            result = {'error':str(error)}
            return JsonResponse(result)
        result = {'result':f'sucessfully added data at {match.id}'}
    return JsonResponse(result)

'''api for delivery'''
@csrf_exempt
def get_delivery(request,id=None):
    if request.method == 'DELETE':
        delivery = Delivery.objects.get(pk=id).delete()
        delivery = {'result':"deleted"}
    elif request.method == 'GET':
        try:
            delivery = Delivery.objects.values().get(pk=id)
        except Delivery.DoesNotExist:
            raise Http404
    return JsonResponse(delivery, safe=False)

@csrf_exempt
def create_delivery(request):
    if request.method == 'POST':
        if request.body:
            data  = json.loads(request.body.decode('utf-8'))
        else:
            return JsonResponse({'error':'no-data'})
        try:
            delivery = Delivery()
            delivery.match          = save_data(data,'match_id')
            delivery.inning         = save_data(data,'inning')
            delivery.batting_team   = save_data(data,'batting_team')
            delivery.bowling_team   = save_data(data,'bowling_team')
            delivery.over           = save_data(data,'over')
            delivery.ball           = save_data(data,'ball')
            delivery.batsman        = save_data(data,'batsman')
            delivery.non_striker    = save_data(data,'non_striker')
            delivery.bowler         = save_data(data,'bowler')
            delivery.is_super_over  = save_data(data,'is_super_over')
            name = save_data(data,'name')
        except KeyError as e:
            return JsonResponse(str(e),safe=False)
        except Exception as error:
            return JsonResponse(str(error),safe=False)
    delivery = {'data':name}
    return JsonResponse(delivery, safe=False)


def match_get(request,id):
    match = Match.objects.get(pk=id)
    form = MatchForm(instance=match)
    return render(request,'ipl/form.html',{'form':form})

#helper functions for above functions
'''helper function for economical_bowler'''
def economy_helper():
    economy_query_set = Delivery.objects.filter(match__season=2015,is_super_over=0).values('bowler').annotate(runs=(Sum('total_runs')-Sum('bye_runs')-Sum('legbye_runs'))*6.0).annotate(balls=(Count('ball')-Count(Case(When(noball_runs__gt=0, then=1)))-Count(Case(When(wide_runs__gt=0, then=1))))).annotate(economy= Cast(F('runs')/F('balls'), FloatField())).order_by('economy')[:10]

    return economy_query_set

# def teams_helper():
def teams_helper(teams,years):
    teams_list = set()
    team_win_details = dict()
    for team in teams:
        if team['winner'] != None:
            teams_list.add(team['winner'])
    teams_list = list(teams_list)
    teams_list.sort()
    for team in teams_list:
        team_win_details[team] = [0]*len(years)
    for row in teams:
        if row['winner'] != None:
            winner = row['winner']
        total_win = row['total_win']
        year = row['season']
        team_win_details[winner][years.index(year)] = total_win
    return team_win_details