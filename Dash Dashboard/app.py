from dash import Dash, html, dcc, callback, Output, Input
from sqlalchemy import create_engine
from config import engine

import plotly.express as px
import pandas as pd

##header stats
total_albums_q="select count(id) as `Total Albums` from albums"
total_rated_albums_q="select count(id_album) as `Albums Rated` from album_ratings where user_final_rating is not null;"
total_stars_albums_q="select sum(user_final_rating) as `Total Stars Albums` from album_ratings where user_final_rating is not null;"
total_tracks_q="select count(id) as `Total Tracks` from tracks"
total_rated_tracks_q="select count(id_track) as `Tracks Rated` from track_ratings where rating is not null;"
total_stars_tracks_q="select sum(rating) as `Total Stars Tracks` from track_ratings where rating is not null;"

totalAbums_df=pd.read_sql(total_albums_q, engine)
totalRatedAbums_df=pd.read_sql(total_rated_albums_q, engine)
totalStarsAbums_df=pd.read_sql(total_stars_albums_q, engine)
totalTracks_df=pd.read_sql(total_tracks_q, engine)
totalRatedTracks_df=pd.read_sql(total_rated_tracks_q, engine)
totalStarsTracks_df=pd.read_sql(total_stars_tracks_q, engine)

##ratings graf
ratings_albums_q="""select rv.Rating, ifnull(Count,0) Quantity from ratings_values rv left join
(select user_final_rating as Rating, count(user_final_rating) as Count from album_ratings group by user_final_rating) ar
 on rv.Rating = ar.Rating order by 1 desc ;"""

ratings_tracks_q="""select rv.Rating, ifnull(Count,0) Quantity from ratings_values rv left join
(select rating as Rating, count(rating) as Count from track_ratings group by rating) tr
 on rv.Rating = tr.Rating order by 1 desc ;"""

types_q="""select at.name Type, ifnull(t.count,0) Quantity from album_types at
left join (select type_id, count(id) Count from albums group by type_id) t on at.id=t.type_id;"""

ratingsalbum_df = pd.read_sql(ratings_albums_q, engine)
ratingstrack_df = pd.read_sql(ratings_tracks_q, engine)
types_df = pd.read_sql(types_q, engine)




external_script = ["https://tailwindcss.com/", {"src": "https://cdn.tailwindcss.com"}]
app = Dash(
    __name__,
    external_scripts=external_script,
)
app.scripts.config.serve_locally = True

def header_stat(df):
    label = df.columns[0]
    value = df.iloc[0, 0]
    return html.Div([
        html.Div(children=value, className="text-4xl text-center"),
        html.Div(children=label, className="text-xl text-center")        
    ],className="w-1/6 h-auto flex flex-col text-white rounded-lg bg-gray-100 p-4 m-4 bg-gradient-to-br from-gray-400 to-black")

def ratings_graf1():
     fig = px.pie(types_df, values='Quantity', names='Type', title='Albums by Type', height=335)

     return html.Div([
        #   dcc.Graph(
        #     id='types-graph',
        #     figure=fig
        #     )
    ],className="h-1/2 bg-gradient-to-br from-blue-400 to-black")


def ratings_graf2():
    fig = px.bar(ratingsalbum_df, y='Rating', x='Quantity', title='Albums by Rating', height=335, orientation='h')
    return html.Div([
        # dcc.Graph(
        #     id='albums-graph',
        #     figure=fig
        #     )
          
    ],className="h-1/2 bg-gradient-to-br from-red-400 to-black")


def ratings_graf3():
     fig = px.bar(ratingstrack_df, x='Rating', y='Quantity', title='Tracks by Rating', height=335)
     return html.Div([
            # dcc.Graph( 
            # id='tracks-graph',
            # figure=fig
            # )
          
    ],className="h-1/2 bg-gradient-to-br from-blue-400 to-black")


def ratings_graf4():
    return html.Div([          
    ],className="h-1/2 bg-gradient-to-br from-red-400 to-black")

def activity_table():
     return html.Div([
          
    ],className="w-full bg-gradient-to-br from-green-400 to-black")
   

app.layout = html.Div([
   ##hdashboard header
    html.Div([
        header_stat(totalAbums_df),
        header_stat(totalRatedAbums_df),
        header_stat(totalStarsAbums_df),
        header_stat(totalTracks_df),
        header_stat(totalRatedTracks_df),
        header_stat(totalStarsTracks_df) 
    ], className="flex flex-row justify-center px-[50px] mb-[50px]"),

    ##dashboard body


    html.Div([
    ##graf container
        html.Div([            
            #row 1
            html.Div([
                ratings_graf1(),
                html.Div('',className="m-3"),               
                ratings_graf2()
            ],className="flex flex-col w-1/2 mx-3"),
            #row 2
            html.Div([
                ratings_graf3(),
                html.Div('',className="m-3"),         
                ratings_graf4()
            ], className="flex flex-col w-1/2 mx-3")                 
        ], className="flex w-2/4"),
        
        ##table container
        html.Div([
            activity_table()
        ],className="flex w-1/4 flex-row mx-3"),

    ],className="flex justify-center w-full h-full")

],className="flex flex-col bg-gradient-to-br from-red-800 to-blue w-full h-[900px] pb-[50px]")


if __name__ == '__main__':
    app.run(debug=False)
