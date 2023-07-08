from dash import Dash, html, dcc
from config import engine
import plotly.express as px
import pandas as pd



##header stats
total_albums_q="select count(id) as `Total Albums` from albums"
total_rated_albums_q="select count(id_album) as `Albums Rated` from album_ratings where user_final_rating is not null;"
total_stars_albums_q="select avg(user_final_rating) as `Average Album Rating` from album_ratings where user_final_rating is not null;"
total_tracks_q="select count(id) as `Total Tracks` from tracks"
total_rated_tracks_q="select count(id_track) as `Tracks Rated` from track_ratings where rating is not null;"
total_stars_tracks_q="select avg(rating) as `Average Track Rating` from track_ratings where rating is not null;"

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

##activiry query
activity_q="""select  al.name Album, art.name Artist, ar.user_final_rating Rating, ar.updated_date Date, al.cover_url Cover from album_ratings ar left join albums al on ar.id_album = al.id 
left join artists art on art.id = al.artist_id
where ar.user_final_rating is not null 
order by 4 desc limit 20;"""

activity_df = pd.read_sql(activity_q, engine)




external_script = ["https://tailwindcss.com/", {"src": "https://cdn.tailwindcss.com"}]
app = Dash(
    __name__,
    external_scripts=external_script,
)
app.scripts.config.serve_locally = True



def header_stat(df):
    label = df.columns[0]
    value = df.iloc[0, 0]
    value = "%.2f" % value if isinstance(value, float) else value
    return html.Div([
        html.Div(children=value, className="text-4xl font-bold text-center"),
        html.Div(children=label, className="text-xl text-center")        
    ],className="w-1/6 h-auto flex flex-col text-white rounded-lg bg-gray-100 p-4 m-4 bg-gradient-to-br from-gray-800 to-black")

def types_graf():
     fig = px.pie(types_df, values='Quantity', names='Type', color_discrete_sequence=px.colors.sequential.Turbo)
     fig.update_layout(autosize=True)
     fig.update_layout(margin_t=100)
     fig.update_layout(margin_b=40)             
     fig.update_layout(title_text='Albums by Type', title_font_size=20, title_font_color='white')
     fig.update_layout(paper_bgcolor='rgb(0,0,0,0)')
     fig.update_layout(font_color='white')
     return html.Div([
          dcc.Graph(
            id='types-graph',
            figure=fig,  style={'height': '100%'}        
            )
    ],className="h-1/2 rounded-lg bg-gradient-to-br from-gray-800 to-black")


def album_ratings_graf():
    fig = px.bar(ratingsalbum_df, y='Rating', x='Quantity',title='Albums by Rating', orientation='h')
    fig.update_traces(marker_color='rgb(50,20,60)')
    fig.update_layout(autosize=True)
    fig.update_xaxes(visible=True, fixedrange=True)   
    fig.update_yaxes(visible=True, fixedrange=True)        
    fig.update_layout(title_font_size=20, title_font_color='white')
    fig.update_layout(paper_bgcolor='rgb(0,0,0,0)')
    fig.update_layout(font_color='white')
    fig.update_layout(plot_bgcolor='rgb(24,24,24)')
    fig.update_layout(
        yaxis = dict(
            tickmode = 'linear',
            tick0 = 0.5,
            dtick = 0.5
        )
    )
    return html.Div([
        dcc.Graph(
            id='albums-graph',
            figure=fig,
            style={'height': '100%'}          
            )          
    ],className="h-1/2 rounded-lg bg-gradient-to-tr from-gray-800 to-black")


def track_ratings_graph():
     fig = px.bar(ratingstrack_df, x='Rating', y='Quantity', title='Tracks by Rating')
     fig.update_traces(marker_color='rgb(50,20,60)')
     fig.update_layout(autosize=True) 
     fig.update_xaxes(visible=True, fixedrange=True)   
     fig.update_yaxes(visible=True, fixedrange=True)    
     fig.update_layout(title_font_size=20, title_font_color='white')
     fig.update_layout(paper_bgcolor='rgb(0,0,0,0)')
     fig.update_layout(font_color='white')
     fig.update_layout(plot_bgcolor='rgb(24,24,24)')
     fig.update_layout(
        xaxis = dict(
            tickmode = 'linear',
            tick0 = 0.5,
            dtick = 0.5
        )
     )
     return html.Div([
            dcc.Graph( 
            id='tracks-graph',
            figure=fig,
            style={'height': '100%'}            )          
    ],className="h-1/2 rounded-lg bg-gradient-to-bl from-gray-800 to-black")

def activity_trend_graf():
    activity_df['IndexValues'] =  activity_df.index
    fig = px.line(activity_df, y='Rating', x='IndexValues', title='Latest Ratings Trend', markers=True, 
                  hover_data={'IndexValues':False,'Album':True, 'Date':True  })
    fig.update_layout(hoverlabel_font_color='white') 
    fig.update_layout(autosize=True)
    fig.update_xaxes(autorange="reversed")    
    fig.update_xaxes(visible=False, fixedrange=True)
    fig.update_yaxes(visible=True, fixedrange=True)      
    fig.update_layout(title_font_size=20, title_font_color='white')
    fig.update_layout(paper_bgcolor='rgb(0,0,0,0)')
    fig.update_traces(marker_color='rgb(50,160,250)') 
    fig.update_traces(line_color='rgb(50,160,250)')   
    fig.update_layout(plot_bgcolor='rgb(24,24,24)')  
    fig.update_layout(yaxis_range=[0.5,5.4], yaxis_tickmode='linear', yaxis_tick0=0.5, yaxis_dtick=0.5)
    
    fig.update_layout(font_color='white')  
    return html.Div([
            dcc.Graph( 
            id='trend-graph',
            figure=fig,
            style={'height': '100%'}            )          
    ],className="h-1/2 rounded-lg bg-gradient-to-tl from-gray-800 to-black")



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
    ], className="flex flex-row justify-center px-[50px]"),
    ##dashboard body
    html.Div([
    ##graf container
        html.Div([            
            #col 1
            html.Div([
                types_graf(),
                html.Div('',className="m-3"),               
                album_ratings_graf()
            ],className="flex flex-col w-1/2 mx-3"),
            #col 2
            html.Div([
                track_ratings_graph(),
                html.Div('',className="m-3"),         
                activity_trend_graf()
            ], className="flex flex-col w-1/2 mx-3")                 
        ], className="flex w-4/5"),  

    ],className="flex justify-center w-full h-full")

],className="flex flex-col w-full h-[900px] pb-[50px]")
#bg-gradient-to-br from-red-800 to-blue 


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0") 