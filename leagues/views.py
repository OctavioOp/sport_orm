from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Count

from . import team_maker


def index(request):

    baseball = League.objects.filter(name__contains='Baseball')
    women_league = League.objects.filter(name__contains='women')
    hockey_league = League.objects.filter(sport__contains='hockey')
    not_football = League.objects.exclude(sport='soccer')
    conference = League.objects.filter(name__contains='conference')
    atlanta = Team.objects.filter(location='Atlanta')
    dallas = Team.objects.filter(location='Dallas')
    raptors = Team.objects.filter(team_name__contains='Raptors')
    city = Team.objects.filter(location__contains='city')
    ti = Team.objects.filter(team_name__startswith='T')
    order = Team.objects.order_by('location')
    Iorder = Team.objects.order_by('-team_name')
    cooper = Player.objects.filter(last_name='Cooper')
    joshua = Player.objects.filter(first_name='Joshua')
    josh = Player.objects.filter(
        last_name='Cooper') & Player.objects.exclude(first_name='Joshua')
    aw = Player.objects.filter(
        first_name='Alexander') | Player.objects.filter(first_name='Wyatt')
    # second part
    atlantic = Team.objects.filter(league__name='Atlantic Soccer Conference')
    player_boston = Player.objects.filter(
        curr_team__team_name='Penguin', curr_team__location='Boston')
    jugadores = Player.objects.filter(
        curr_team__league__name='International Collegiate Baseball Conference')
    amateur_soccer = Player.objects.filter(
        curr_team__league__name='American Amateur Soccer Conference').filter(last_name='Lopez')
    soccer = Player.objects.filter(all_teams__league__sport='Soccer')
    sophia = Team.objects.filter(curr_players__first_name='Sophia')
    sophia_leagues = League.objects.filter(
        teams__curr_players__first_name='Sophia')
    flores = Player.objects.filter(last_name='FLores').exclude(
        curr_team__team_name='Washington Roughriders')
    evans = Team.objects.filter(all_players__first_name='Samuel', all_players__last_name='Evans') & Team.objects.filter(
        curr_players__first_name='Samuel', curr_players__last_name='Evans')
    thunder_cat = Player.objects.filter(
        all_teams__team_name='Tigers') | Player.objects.filter(curr_team__team_name='Tigers')
    # whichitas team

    try:
        loswichitavikin = Team.objects.get(
            team_name="Vikings", location="Wichita")
        wichita_players = loswichitavikin.all_players.all()
        wichita_current_ids = [
            player.id for player in loswichitavikin.curr_players.all()]
        not_now_wichita = [
            player for player in wichita_players if player.id not in wichita_current_ids]

    except Team.DoesNotExist:
        not_now_wichita = []

    joshuas2 = Player.objects.filter(first_name='Joshua') & Player.objects.filter(
        all_teams__league__name='Atlantic Federation of Collegiate Baseball Athletics')
    team12 = Team.objects.annotate(Count('curr_players')).annotate(Count(
        'all_players')).filter(curr_players__count__gte=12).filter(all_players__count__gte=12)
    orderplayer = Player.objects.annotate(
        Count('all_teams')).order_by('all_teams__count')

    '''
	Detroit colt 4 
	try:
		loswichitavikin = Team.objects.get(team_name = "Vikings", location = "Wichita")
		wichita_players = loswichitavikin.all_players.all()
		wichita_current_ids = [player.id for player in loswichitavikin.curr_players.all()]
		not_now_wichita = [player for player in wichita_players if player.id not in wichita_current_ids]

	except Team.DoesNotExist:
		not_now_wichita = []
'''
    # jacob 12

    context = {
        "leagues": League.objects.all(),
        "teams": Team.objects.all(),
        "players": Player.objects.all(),
        'baseball': baseball,
        'women_league': women_league,
        'hockey_league': hockey_league,
        'not_football': not_football,
        'conference': conference,
        'atlanta': atlanta,
        'dallas': dallas,
        'raptor': raptors,
        'city': city,
        'ti': ti,
        'order': order,
        'Iorder': Iorder,
        'cooper': cooper,
        'joshua': joshua,
        'josh': josh,
        'aw': aw,
        'atlantic': atlantic,
        'player_boston': player_boston,
        'jugadores': jugadores,
        'amateur_soccer': amateur_soccer,
        'soccer': soccer,
        'sophia': sophia,
        'sophia_leagues': sophia_leagues,
        'flores': flores,
        'evans': evans,
        'thunder_cat': thunder_cat,
        'not_now_wichita': not_now_wichita,
        'joshuas2': joshuas2,
        'team12': team12,
        'orderplayer': orderplayer

    }
    return render(request, "leagues/index.html", context)


def make_data(request):
    team_maker.gen_leagues(10*2)
    team_maker.gen_teams(50*2)
    team_maker.gen_players(200*2)

    return redirect("index")
