from django.shortcuts import render
import pandas as pd
from rest_framework.response import Response
from rest_framework.decorators import api_view

df=pd.read_csv("static/olympics_dataset.csv")
# Create your views here.

def index(request):
    return render(request,'home.html')

def medal_over_time(request):
    return render(request,'medal_over_time.html')

def medal_distribution_breakdown(request):
    
    return render(request,'medal_distribution_breakdown.html')

def country_sports_comparison(request):
    return render(request,'country_sports_comparison.html')

def participation_and_athlete(request):
    return render(request,'participation_and_athlete.html')

def summary(request):
    return render(request,'summary.html')

def help(request):
    return render(request,'help.html')
@api_view(['GET'])
def MedalsByCountryYearView(request):
    if request.method=="GET":
        medals_by_country_year = df[df['Medal'] != 'No medal'].groupby(['Year', 'Team']).size().reset_index(name='Total Medals')
        data = medals_by_country_year.to_dict(orient='records')
        return Response(data)

@api_view(['GET'])
def MedalsByGenderYearView(request):
    medals_by_gender_year = df[df['Medal'] != 'No medal'].groupby(['Year', 'Sex']).size().reset_index(name='Medals')
    data = medals_by_gender_year.to_dict(orient='records')
    return Response(data)


@api_view(['GET'])
def CumulativeMedalsTopCountriesView(request):
    top_5_countries = df[df['Medal'] != 'No medal']['Team'].value_counts().head(5).index
    filtered_df = df[(df['Medal'] != 'No medal') & (df['Team'].isin(top_5_countries))]
    medals_cumulative = filtered_df.groupby(['Year', 'Team']).size().unstack(fill_value=0).cumsum()
    data = {
        'years': medals_cumulative.index.tolist(),
        'countries': {}
    }
    for country in top_5_countries:
        data['countries'][country] = medals_cumulative[country].tolist()
    return Response(data)

@api_view(['GET'])
def MedalsBySportYearView(request):
    # Group by Year and Sport, then count the medals
    medals_by_sport_year = df[df['Medal'] != 'No medal'].groupby(['Year', 'Sport']).size().reset_index(name='Total Medals')
    
    # Convert the DataFrame to a dictionary for JSON response
    data = {
        'years': medals_by_sport_year['Year'].tolist(),
        'sports': medals_by_sport_year['Sport'].tolist(),
        'total_medals': medals_by_sport_year['Total Medals'].tolist()
    }

    # Return the data as a JSON response
    return Response(data)

@api_view(['GET'])
def MedalsOverTimeView(request):
    # Group the data by Year to count the number of medals
    medals_over_time = df.groupby('Year')['Medal'].count().reset_index()

    # Convert the DataFrame to a dictionary for JSON response
    data = {
        'years': medals_over_time['Year'].tolist(),
        'medals': medals_over_time['Medal'].tolist(),
    }

    # Return the data as a JSON response
    return Response(data)

@api_view(['GET'])
def AthletesOverTimeView(request):
    # Group the data by Year to count the number of unique athletes
    athletes_over_time = df.groupby('Year')['player_id'].nunique().reset_index()

    # Convert the DataFrame to a dictionary for JSON response
    data = {
        'years': athletes_over_time['Year'].tolist(),
        'athletes': athletes_over_time['player_id'].tolist(),
    }

    # Return the data as a JSON response
    return Response(data)
@api_view(['GET'])
def Top10CountriesMedalsView(request):
    # Group the data by Team to count the total medals
    df_medal_count = df.groupby('Team')['Medal'].count().reset_index()

    # Sort and get the top 10 countries
    df_top10_countries = df_medal_count.sort_values('Medal', ascending=False).head(10)

    # Convert the DataFrame to a dictionary for JSON response
    data = {
        'countries': df_top10_countries['Team'].tolist(),
        'medals': df_top10_countries['Medal'].tolist(),
    }

    # Return the data as a JSON response
    return Response(data)

@api_view(['GET'])
def Top10CountriesMedalsView(request):
    # Group the data by Team to count the total medals
    df_medal_count = df.groupby('Team')['Medal'].count().reset_index()

    # Sort and get the top 10 countries
    df_top10_countries = df_medal_count.sort_values('Medal', ascending=False).head(10)

    # Convert the DataFrame to a dictionary for JSON response
    data = {
        'countries': df_top10_countries['Team'].tolist(),
        'medals': df_top10_countries['Medal'].tolist(),
    }

    # Return the data as a JSON response
    return Response(data)

@api_view(['GET'])
def Top10Countries2024MedalsView(request):
    # Filter data for the year 2024
    df_2024 = df[df['Year'] == 2024]

    # Group the data by Team to count the total medals in 2024
    df_medal_count_2024 = df_2024.groupby('Team')['Medal'].count().reset_index()

    # Sort and get the top 10 countries by medals
    df_top10_countries_2024 = df_medal_count_2024.sort_values('Medal', ascending=False).head(10)

    # Convert the DataFrame to a dictionary for JSON response
    data = {
        'countries': df_top10_countries_2024['Team'].tolist(),
        'medals': df_top10_countries_2024['Medal'].tolist(),
    }

    # Return the data as a JSON response
    return Response(data)

@api_view(['GET'])
def TotalMedalsOverTimeView(request):
    # Group the data by Year to count the total medals
    medals_over_time = df.groupby('Year')['Medal'].count().reset_index()

    # Convert the DataFrame to a dictionary for JSON response
    data = {
        'years': medals_over_time['Year'].tolist(),
        'medals': medals_over_time['Medal'].tolist(),
    }

    # Return the data as a JSON response
    return Response(data)

@api_view(['GET'])
def TopSportsByMedalCountView(request):
    # Count medals by sport and get the top 10
    medals_by_sport = df['Sport'].value_counts().head(10)

    # Convert the Series to a dictionary for JSON response
    data = {
        'sports': medals_by_sport.index.tolist(),
        'medal_counts': medals_by_sport.values.tolist(),
    }

    # Return the data as a JSON response
    return Response(data)

@api_view(['GET'])
def MedalsByCountryOverTimeView(request):
    # Prepare the data by grouping and counting medals by year and country
    medals_by_country_year = df[df['Medal'] != 'No medal'].groupby(['Year', 'Team']).size().reset_index(name='Total Medals')

    # Convert the DataFrame to a dictionary for JSON response
    data = {
        'years': medals_by_country_year['Year'].tolist(),
        'teams': medals_by_country_year['Team'].tolist(),
        'total_medals': medals_by_country_year['Total Medals'].tolist(),
    }

    # Return the data as a JSON response
    return Response(data)

@api_view(['GET'])
def GoldMedalsBySportView(request):
    # Filter data for the year 2024
    df_2024 = df[df['Year'] == 2024]
    
    # Get the top country with the most gold medals
    top_country_2024 = df_2024[df_2024['Medal'] == 'Gold'].groupby('Team').count().reset_index().sort_values('Medal', ascending=False).iloc[0]['Team']
    
    # Filter data for that country and gold medals
    df_top_country_2024 = df_2024[(df_2024['Team'] == top_country_2024) & (df_2024['Medal'] == 'Gold')]
    
    # Prepare data for pie chart
    data = {
        'sports': df_top_country_2024['Sport'].tolist(),
        'gold_medals': df_top_country_2024['Medal'].count(),
        'top_country': top_country_2024,
    }

    return Response(data)

@api_view(['GET'])
def GoldMedalsBySportAllTimeView(request):
    # Filter data for all time
    df_all_time = df[df['Year'] <= 2024]
    
    # Get the top country with the most gold medals across all time
    top_country_all_time = df_all_time[df_all_time['Medal'] == 'Gold'].groupby('Team').count().reset_index().sort_values('Medal', ascending=False).iloc[0]['Team']
    
    # Filter data for that country and gold medals
    df_top_country_all_time = df_all_time[(df_all_time['Team'] == top_country_all_time) & (df_all_time['Medal'] == 'Gold')]
    
    # Prepare data for pie chart
    data = {
        'sports': df_top_country_all_time['Sport'].tolist(),
        'gold_medals': df_top_country_all_time['Medal'].count(),
        'top_country': top_country_all_time,
    }

    return Response(data)

@api_view(['GET'])
def MedalsDistributionHeatmapView(request):
    # Filter data for countries with medals
    top_countries = df[df['Medal'] != 'No medal']['Team'].value_counts().head(10).index
    filtered_df = df[(df['Medal'] != 'No medal') & (df['Team'].isin(top_countries))]

    # Group the data by Year and Team
    medals_by_country_year = filtered_df.groupby(['Year', 'Team']).size().unstack(fill_value=0)

    # Prepare the data for the heatmap
    data = {
        'z': medals_by_country_year.values.tolist(),  # Heatmap values
        'x': medals_by_country_year.columns.tolist(),  # Team names (x-axis)
        'y': medals_by_country_year.index.tolist()     # Years (y-axis)
    }

    return Response(data)

@api_view(['GET'])
def MedalsByGenderAndSportView(request):
    # Filter data to exclude 'No medal'
    medals_by_gender_sport = df[df['Medal'] != 'No medal'].groupby(['Sport', 'Sex']).size().reset_index(name='Count')

    # Prepare the data for the bar chart
    data = medals_by_gender_sport.to_dict(orient='records')

    return Response(data)

@api_view(['GET'])
def TopAthletesView(request):
    # Filter data to exclude 'No medal'
    top_athletes = df[df['Medal'] != 'No medal'].groupby(['Name', 'Medal']).size().unstack(fill_value=0).reset_index()
    top_athletes['Total'] = top_athletes[['Gold', 'Silver', 'Bronze']].sum(axis=1)
    top_10_athletes = top_athletes.sort_values('Total', ascending=False).head(10)

    # Melt the DataFrame for Plotly
    top_10_athletes_melted = top_10_athletes.melt(id_vars=['Name'], value_vars=['Gold', 'Silver', 'Bronze'],
                                                  var_name='Medal', value_name='Count')

    # Prepare the data for the bar chart
    data = top_10_athletes_melted.to_dict(orient='records')

    return Response(data)

@api_view(['GET'])
def TopCountriesParticipationView(request):
    # Count participants by country (NOC)
    country_participation = df['NOC'].value_counts()
    
    # Get the top 10 countries
    top_10_countries = country_participation.head(10).reset_index()
    top_10_countries.columns = ['Country', 'Number of Participants']

    # Prepare the data for the bar chart
    data = top_10_countries.to_dict(orient='records')

    return Response(data)

@api_view(['GET'])
def ParticipationOverviewView(request):
    gender_data = df.groupby(['Year', 'Sex']).size().unstack(fill_value=0)
    gender_data['Total'] = gender_data.sum(axis=1)

    # Get the top 5 countries based on total participation
    top_countries = df['Team'].value_counts().head(5).index

    # Group data by year and top 5 countries to count participants
    countries_data = df[df['Team'].isin(top_countries)].groupby(['Year', 'Team']).size().unstack(fill_value=0)

    # Prepare the data for response
    response_data = {
        "gender_data": gender_data.to_dict(),
        "top_countries": top_countries.tolist(),
        "countries_data": countries_data.to_dict()
    }

    return Response(response_data)

@api_view(['GET'])
def OlympicParticipationOverviewView(request):
    
    total_participants = df.groupby('Year').size()

    # 2. Total gold medals won over time
    gold_medals = df[df['Medal'] == 'Gold']
    gold_medals_per_year = gold_medals.groupby('Year').size()

    # 3. Top 5 countries by number of participants
    top_5_participating_countries = df['Team'].value_counts().head(5).index
    top_5_participants = df[df['Team'].isin(top_5_participating_countries)].groupby(['Year', 'Team']).size().unstack(fill_value=0)

    # 4. Top 5 countries by number of gold medals won
    top_5_gold_countries = gold_medals['Team'].value_counts().head(5).index
    top_5_gold_winners = gold_medals[gold_medals['Team'].isin(top_5_gold_countries)].groupby(['Year', 'Team']).size().unstack(fill_value=0)

    # Prepare the data for response
    response_data = {
        "total_participants": total_participants.to_dict(),
        "gold_medals_per_year": gold_medals_per_year.to_dict(),
        "top_5_participants": top_5_participants.to_dict(),
        "top_5_gold_winners": top_5_gold_winners.to_dict(),
        "top_5_participating_countries": top_5_participating_countries.tolist(),
        "top_5_gold_countries": top_5_gold_countries.tolist(),
    }

    return Response(response_data)
@api_view(['GET'])
def top_3_participants_view(request):
    year_country_data = df.groupby(['Year', 'Team']).size().unstack(fill_value=0)

    # Create an empty DataFrame to store results
    top_3_participants = []

    # Iterate through each year to calculate the total participants of top 3 countries
    for year in year_country_data.index:
        year_data = year_country_data.loc[year]
        top_3_countries = year_data.nlargest(3).index
        for country in top_3_countries:
            top_3_participants.append({
                'Year': year,
                'Country': country,
                'Participants': year_data[country]
            })
    print(type(top_3_participants))
    return Response(top_3_participants)

@api_view(['GET'])
def kpis(request):
    print(df.columns)
    total_athletes = df['Name'].nunique()
    total_teams = df['Team'].nunique()
    total_events = df['Event'].nunique()
    total_medals = df[df['Medal'].notna()].shape[0]
    medal_count_by_sex = df[df['Medal'].notna()].groupby('Sex').size()
    male_percentage = (medal_count_by_sex.get('M', 0) / medal_count_by_sex.sum()) * 100
    top_sports = df[df['Medal'].notna()].groupby('Sport').size().nlargest(1)

    return Response({
        'total_athletes': total_athletes,
        'total_teams': total_teams,
        'total_events': total_events,
        'total_medals': total_medals,
        'male_percentage': round(male_percentage,2),
        'top_sports': top_sports[0]
    })

@api_view(['GET'])
def MedalCountBySexView(request):
    medal_count_by_sex = df[df['Medal'].notna()].groupby('Sex').size()
    total_medals = medal_count_by_sex.sum()
    percentage_male = (medal_count_by_sex.get('M', 0) / total_medals) * 100 if total_medals > 0 else 0
    percentage_female = (medal_count_by_sex.get('F', 0) / total_medals) * 100 if total_medals > 0 else 0
    return Response({'Male': percentage_male, 'Female': percentage_female})


@api_view(['GET'])
def TopSportsView(request):
    top_sports = (df[df['Medal'].notna()]
                    .groupby('Sport').size()
                    .nlargest(5)
                    .reset_index(name='count')
                    .to_dict(orient='records'))
    return Response(top_sports)


@api_view(['GET'])
def MedalsByYearView(request):
    medals_by_year = (df[df['Medal'].notna()]
                        .groupby('Year').size()
                        .reset_index(name='count')
                        .to_dict(orient='records'))
    return Response(medals_by_year)


@api_view(['GET'])
def MedalDistributionBySeasonView(request):
    medal_distribution_by_season = (df[df['Medal'].notna()]
                                    .groupby('Season').size()
                                    .reset_index(name='count')
                                    .to_dict(orient='records'))
    return Response(medal_distribution_by_season)

@api_view(['GET'])
def MedalsByCountryView(request):
    medals_by_country = (
        df[df['Medal'].notna()]
        .groupby('NOC')
        .size()
        .reset_index(name='count')
        .sort_values(by='count', ascending=False)
        .head(10)
        .to_dict(orient='records')
    )
    return Response(medals_by_country)