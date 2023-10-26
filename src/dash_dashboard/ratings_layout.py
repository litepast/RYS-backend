from dash import html, dcc
import plotly.express as px
import pandas as pd

totalAbums_df = pd.read_csv("./Data/ratings_dashboard/totalAbums.csv")
totalRatedAbums_df =pd.read_csv("./Data/ratings_dashboard/totalRatedAbums.csv")
totalStarsAbums_df = pd.read_csv("./Data/ratings_dashboard/totalStarsAbums.csv")
totalTracks_df = pd.read_csv("./Data/ratings_dashboard/totalTracks.csv")
totalRatedTracks_df = pd.read_csv("./Data/ratings_dashboard/totalRatedTracks.csv")
totalStarsTracks_df = pd.read_csv("./Data/ratings_dashboard/totalStarsTracks.csv")
ratingsalbum_df = pd.read_csv("./Data/ratings_dashboard/ratingsalbum.csv")
ratingstrack_df = pd.read_csv("./Data/ratings_dashboard/ratingstrack.csv")
types_df = pd.read_csv("./Data/ratings_dashboard/types.csv")
activity_df= pd.read_csv("./Data/ratings_dashboard/activity.csv")

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
   

layout = html.Div([
   ##hdashboard header
    html.Div([
        header_stat(totalAbums_df),
        header_stat(totalRatedAbums_df),
        header_stat(totalStarsAbums_df),
        header_stat(totalTracks_df),
        header_stat(totalRatedTracks_df),
        header_stat(totalStarsTracks_df) 
    ], className="flex flex-row justify-center"),
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
        ], className="flex w-full"),  

    ],className="flex justify-center w-full h-full")

],className="flex flex-col w-full h-full")
