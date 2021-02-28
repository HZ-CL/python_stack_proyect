from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
    li_baseball = League.objects.filter(sport='Baseball')
    li_women = League.objects.filter(name__icontains='women')
    li_hockey = League.objects.filter(sport__icontains='hockey')
    li_futbol = League.objects.filter(sport__icontains='football')
    li_confere = League.objects.filter(name__icontains='conference')
    ligas_all = League.objects.all()
    li_regioni =Team.objects.filter(location='Atlanta')
    team_dallas = Team.objects.filter(location__icontains='dallas')
    team_raptors = Team.objects.filter(team_name__icontains='raptor')
    team_city = Team.objects.filter(location__icontains='city')
    team_tt = Team.objects.filter(team_name__istartswith="t")
    team_order_loc = Team.objects.all().order_by("location")
    team_order_name = Team.objects.all().order_by("-team_name")
    ply_last_name =Player.objects.filter(last_name="Cooper")
    ply_first_name = Player.objects.filter(first_name="Joshua")
    ply_first_except_c = ply_last_name.exclude(first_name="Joshua")
    ply_mult_filt = Player.objects.filter(first_name="Alexander")|Player.objects.filter(first_name="Wyatt")


    context = {
		"leagues": ligas_all,
		"filt_baseball":li_baseball,
		"filt_women": li_women,
		"filt_hockey": li_hockey,
		"filt_football": li_futbol,
		"conference": li_confere,
        "filt_region": li_regioni,
		"teams": Team.objects.all(),
		"flit_dallas":team_dallas,
		"filt_raptors": team_raptors,
		"filt_city": team_city,
		"filt_start_t": team_tt,
		"filt_order_alf": team_order_loc,
		"filt_order_name": team_order_name,
		"players": Player.objects.all(),
		"players_lastname": ply_last_name,
		"players_firstname":ply_first_name,
		"players_frist_except": ply_first_except_c,
		"players_multi": ply_mult_filt,
	}
    return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")






