from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="index"),
    path("medal_over_time/",views.medal_over_time,name="medal_over_time"),
    path("medal_distribution_breakdown/",views.medal_distribution_breakdown,name="medal_distribution_breakdown"),
    path("country_sports_comparison/",views.country_sports_comparison,name="country_sports_comparison"),
    path("participation_and_athlete/",views.participation_and_athlete,name="participation_and_athlete"),
    path("summary/",views.summary,name="summary"),
    path('help/',views.help,name="help"),
    path("api/MedalsByCountryYearView/",views.MedalsByCountryYearView,name="MedalsByCountryYearView"),
    path("api/MedalsByGenderYearView/",views.MedalsByGenderYearView,name="MedalsByGenderYearView"),
    path("api/CumulativeMedalsTopCountriesView/",views.CumulativeMedalsTopCountriesView,name="CumulativeMedalsTopCountriesView"),
    path("api/MedalsBySportYearView/",views.MedalsBySportYearView,name="MedalsBySportYearView"),
    path('api/medals-over-time/', views.MedalsOverTimeView, name='medals_over_time'),
    path('api/medals-over-time/', views.MedalsOverTimeView, name='medals_over_time'),
    path('api/top-10-countries-medals/', views.Top10CountriesMedalsView, name='top_10_countries_medals'),
    path('api/top-10-countries-2024-medals/', views.Top10Countries2024MedalsView, name='top_10_countries_2024_medals'),
    path('api/total-medals-over-time/', views.TotalMedalsOverTimeView, name='total_medals_over_time'),
    path('api/top-sports-by-medal-count/', views.TopSportsByMedalCountView, name='top_sports_by_medal_count'),
    path('api/medals-by-country-over-time/', views.MedalsByCountryOverTimeView, name='medals_by_country_over_time'),
    path('api/gold-medals-by-sport/', views.GoldMedalsBySportView, name='gold_medals_by_sport'),
    path('api/gold-medals-by-sport-all-time/', views.GoldMedalsBySportAllTimeView, name='gold_medals_by_sport_all_time'),
    path('api/medals-distribution-heatmap/', views.MedalsDistributionHeatmapView, name='medals_distribution_heatmap'),
    path('api/medals-gender-sport/', views.MedalsByGenderAndSportView, name='medals_by_gender_sport'),
    path('api/top-athletes/', views.TopAthletesView, name='top_athletes'),
    path('api/top-countries-participation/',views. TopCountriesParticipationView, name='top_countries_participation'),
    path('api/participation-overview/', views.ParticipationOverviewView, name='participation_overview'),
    path('api/olympic-participation-overview/', views.OlympicParticipationOverviewView, name='olympic_participation_overview'),
    path('api/top-3-participants/', views.top_3_participants_view, name='top-3-participants'),
    path('api/kpis/', views.kpis, name='kpis'),
    path('api/medal-count-by-sex/', views.MedalCountBySexView, name='medal_count_by_sex'),
    path('api/top-sports/', views.TopSportsView, name='top_sports'),
    path('api/medals-by-year/', views.MedalsByYearView, name='medals_by_year'),
    path('api/medal-distribution-by-season/', views.MedalDistributionBySeasonView, name='medal_distribution_by_season'),
    path("api/MedalsByCountryView/",views.MedalsByCountryView,name="MedalsByCountryView"),


]



