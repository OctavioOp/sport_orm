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
		'aw': aw
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")