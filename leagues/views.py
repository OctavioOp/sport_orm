from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	baseball = League.objects.filter(name__contains = 'Baseball')
	women_league = League.objects.filter(name__contains = 'women')
	hockey_league = League.objects.filter(sport__contains= 'hockey')
	not_football = League.objects.exclude(sport = 'soccer')
	conference = League.objects.filter(name__contains = 'conference')
	atlanta = Team.objects.filter(location = 'Atlanta')
	dallas = Team.objects.filter(location = 'Dallas')
	raptors = Team.objects.filter(team_name__contains = 'Raptors')
	city = Team.objects.filter(location__contains = 'city')
	ti = Team.objects.filter(team_name__startswith ='T')
	order = Team.objects.order_by('location')
	Iorder = Team.objects.order_by('-team_name')
	cooper = Player.objects.filter(last_name = 'Cooper')
	joshua = Player.objects.filter(first_name = 'Joshua')
	josh = Player.objects.filter(last_name = 'Cooper') & Player.objects.exclude(first_name = 'Joshua')
	aw = Player.objects.filter(first_name = 'Alexander') | Player.objects.filter(first_name = 'Wyatt')
	#second part
	atlantic = Team.objects.filter(league__name= 'Atlantic Soccer Conference')
	player_boston = Player.objects.filter(curr_team__team_name='Boston Penguin')
	jugadores = Player.objects.filter(curr_team__league__name ='International Collegiate Baseball Conference')
	amateur_soccer=Player.objects.filter(curr_team__league__name = 'American Amateur Soccer Conference').filter(last_name = 'Lopez')
	soccer = Player.objects.filter(all_teams__league__sport= 'Soccer')
	sophia = Team.objects.filter(curr_players__first_name = 'Sophia')

	'''
	try:
		loswichitavikin = Team.objects.get(team_name = "Vikings", location = "Wichita")
		wichita_players = loswichitavikin.all_players.all()
		wichita_current_ids = [player.id for player in loswichitavikin.curr_players.all()]
		not_now_wichita = [player for player in wichita_players if player.id not in wichita_current_ids]

	except Team.DoesNotExist:
		not_now_wichita = []
'''

	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		'baseball' : baseball,
		'women_league': women_league,
		'hockey_league': hockey_league,
		'not_football': not_football,
		'conference': conference,
		'atlanta': atlanta,
		'dallas': dallas,
		'raptor': raptors,
		'city': city,
		'ti': ti,
		'order':order,
		'Iorder': Iorder,
		'cooper': cooper,
		'joshua': joshua,
		'josh': josh,
		'aw': aw,

	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")