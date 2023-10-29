from dash import html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from config import project_path

yearsalbum_df = pd.read_csv(project_path+"./Data/years_dashboard/yearsAbums.csv")


def quantity_filters():
     return html.Div([
        html.H1('Albums Count', className="text-2xl font-bold text-white"),
        #Range
        html.Div([
            html.Label('Date Range', className="text-xl text-white"),
            dcc.RadioItems( ['Year', 'Decade'], value='Year',id='date-type', className="text-white" ),  
        ]),        
        #Sort by
        html.Div([
             html.Label('Sort by', className="text-xl text-white"),
            dcc.RadioItems(options=[
                {'label': 'Date', 'value': 'category'},
                {'label': 'Quantity', 'value': 'total'}
            ], value='category', id='sort-type', className="text-white"),             
        ]),
        #Order by
        html.Div([
            html.Label('Order', className="text-xl text-white"),
            dcc.RadioItems(options=[
                {'label': 'Ascending', 'value': 'ascending'},
                {'label': 'Descending', 'value': 'descending'}
            ], value='ascending', id='order-type', className="text-white"),             
        ]), 
        #Rated
        html.Div([
            html.Label('Rating Status', className="text-xl text-white"),
            dcc.Dropdown( options=[
                {'label': 'All Albums', 'value': 'All'},
                {'label': 'Only Rated Albums', 'value': 'Rated'},
                {'label': 'Only Unrated Albums', 'value': 'Unrated'}
            ], value='All', id='rated-type',  clearable=False)             
        ]),
    ],className="w-1/6 h-full flex flex-col justify-between px-[25px] py-[30px] ")

@callback( 
    Output('quantity-albums-graph', 'figure'),   
    Input('date-type', 'value'),
    Input('sort-type', 'value'),
    Input('order-type', 'value'),
    Input('rated-type', 'value'))
def quantity_graph(date_type,sort_type,order_type,rated_type):
    if rated_type == 'All':
        df = yearsalbum_df
    else:
        df = yearsalbum_df[yearsalbum_df['Rated'] == rated_type] 
    fig = px.histogram(df, x=date_type, color='Rated', color_discrete_sequence=['#721bbf', '#0a7d8a'], hover_data={'Rated':False })

    final_order = sort_type+' '+order_type

    if date_type == 'Year':
        fig.update_xaxes(rangeslider_visible=True)

    fig.update_xaxes(type='category') 
    fig.update_xaxes(categoryorder=final_order)    
    fig.update_xaxes(visible=True, fixedrange=True)
    fig.update_yaxes(title_text='Quantity', title_font=dict(size=18, color='white'))   
    fig.update_yaxes(visible=True, fixedrange=True)      
    fig.update_layout(barmode='stack')       
    fig.update_layout(autosize=True)          
    fig.update_layout(title_font_size=20, title_font_color='white')
    fig.update_layout(paper_bgcolor='rgb(0,0,0,0)')
    fig.update_layout(font_color='white')
    fig.update_layout(plot_bgcolor='rgb(24,24,24)')    
    return fig

def rating_filters():
     return html.Div([
        html.H1('Ratings Average', className="text-2xl font-bold text-white"),
        #Range
        html.Div([
            html.Label('Date Range', className="text-xl text-white"),
            dcc.RadioItems( ['Year', 'Decade'], value='Year',id='date-type-r', className="text-white" ),  
        ]),        
        #Sort by
        html.Div([
             html.Label('Sort by', className="text-xl text-white"),
            dcc.RadioItems(options=[
                {'label': 'Date'+' ', 'value': 'category'},
                {'label': 'Average', 'value': 'total'}
            ], value='category', id='sort-type-r', className="text-white"),             
        ]),
        #Order by
        html.Div([
            html.Label('Order', className="text-xl text-white"),
            dcc.RadioItems(options=[
                {'label': 'Ascending', 'value': 'ascending'},
                {'label': 'Descending', 'value': 'descending'}
            ], value='ascending', id='order-type-r', className="text-white"),             
        ]),         
    ],className="w-1/6 h-full flex flex-col justify-between px-[25px] pt-[30px] pb-[100px]")


@callback( 
    Output('rating-albums-graph', 'figure'),   
    Input('date-type-r', 'value'),
    Input('sort-type-r', 'value'),
    Input('order-type-r', 'value'))
def ratings_graph(date_type,sort_type,order_type):
    df = yearsalbum_df[yearsalbum_df['Rated'] == 'Rated'] 
    fig = px.histogram(df, y='Rating', x=date_type, histfunc='avg', color_discrete_sequence=['#721bbf'])  
    final_order = sort_type+' '+order_type

    if date_type == 'Year':
        fig.update_xaxes(rangeslider_visible=True)

    fig.update_xaxes(type='category') 
    fig.update_xaxes(categoryorder=final_order)    
    fig.update_xaxes(visible=True, fixedrange=True)
    fig.update_yaxes(title_text='Quantity', title_font=dict(size=18, color='white'))   
    fig.update_yaxes(visible=True, fixedrange=True) 
    fig.update_layout(
        yaxis = dict(
            tickmode = 'linear',
            tick0 = 0.5,
            dtick = 0.5
        )
    )    
    #fig.update_layout(yaxis_range=[0.5,5.4], yaxis_tickmode='linear', yaxis_tick0=0.5, yaxis_dtick=0.5)     
    fig.update_layout(autosize=True)          
    fig.update_layout(title_font_size=20, title_font_color='white')
    fig.update_layout(paper_bgcolor='rgb(0,0,0,0)')
    fig.update_layout(font_color='white')
    fig.update_layout(plot_bgcolor='rgb(24,24,24)')    
    return fig

layout = html.Div([
        #container
        html.Div([    
            #row1
            html.Div([
                quantity_filters(),               
                html.Div([ dcc.Graph( id='quantity-albums-graph',style={'height': '100%'})],className="w-5/6 h-full")                          
            ],className="flex h-[49%] w-full rounded-lg bg-gradient-to-tr from-gray-800 to-black"),
            #row2
            html.Div([  
                rating_filters(),
                html.Div([ dcc.Graph( id='rating-albums-graph',style={'height': '100%'})],className="w-5/6 h-full")                          
            ], className="flex h-[49%] rounded-lg bg-gradient-to-tr from-gray-800 to-black") 
        ], className="flex flex-col justify-between h-full w-full"),
],className="flex flex-col w-full h-full p-4")
#bg-gradient-to-br from-red-800 to-blue 

