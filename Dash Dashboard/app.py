from dash import Dash, html, dcc, callback, Output, Input
from sqlalchemy import create_engine
from config import engine

import plotly.express as px
import pandas as pd


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
        html.Div(children=value, style={'textAlign':'center'}),
        html.Div(children=label, className="bg-blue-500 text-white text-2xl p-2")        
    ],className="w-1/6 bg-gray-200 border border-gray-400 text-center p-2 m-2")


app.layout = html.Div([
   
    html.Div([
        header_stat(totalAbums_df),
        header_stat(totalRatedAbums_df),
        header_stat(totalStarsAbums_df),
        header_stat(totalTracks_df),
        header_stat(totalRatedTracks_df),
        header_stat(totalStarsTracks_df) 
    ], style={'display':'flex'})
])



# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

# app = Dash(__name__)

# app.layout = html.Div([
#     html.H1(children='Title of Dash App', style={'textAlign':'center'}),
#     dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'),
#     dcc.Graph(id='graph-content')
# ])

# @callback(
#     Output('graph-content', 'figure'),
#     Input('dropdown-selection', 'value')
# )
# def update_graph(value):
#     dff = df[df.country==value]
#     return px.line(dff, x='year', y='pop')

if __name__ == '__main__':
    app.run(debug=True)
