from dash import html, dcc, dash_table
import plotly.express as px
import pandas as pd

avg_style_df = pd.read_csv("./Data/styles_dashboard/avg_style.csv")
no_style_df = pd.read_csv("./Data/styles_dashboard/no_style.csv")
styles_df = pd.read_csv("./Data/styles_dashboard/styles.csv")
avg_genre_df = pd.read_csv("./Data/styles_dashboard/avg_genre.csv")



def genres_treemap():
    fig = px.treemap(styles_df, path=['Tag','Genre','Style','Album'], values='Quantity', color_discrete_sequence=px.colors.qualitative.Pastel1)
    fig.update_layout(autosize=True)
    fig.update_layout(paper_bgcolor='rgb(0,0,0,0)')
    fig.update_layout(font_color='white')
    ##make the font bold
    fig.update_layout(font_size=12)
    fig.update_layout(margin_l=0)
    fig.update_layout(margin_r=0)
    fig.update_layout(margin_b=0)
    fig.update_layout(margin_t=20)
    fig.update_traces(marker=dict(cornerradius=5))
    fig.update_traces(hovertemplate='<b>%{label}</b> Qty: %{value}')
    return html.Div([         
        dcc.Graph(
            id='genres_treemap',
            figure=fig, style={'height': '100%'}    
        )
    ],className="h-full flex-col")

def no_style_table():
     if len(no_style_df):
        return html.Div([
            dash_table.DataTable(
                    id='datatable-no-style',
                    columns=[
                        {"name": i, "id": i} for i in no_style_df.columns
                    ],
                    data=no_style_df.to_dict('records'),          
                    page_size=4,
                    sort_action="native",
                    sort_mode="multi",
                    cell_selectable=False,
                    css=[ 
                        {'selector': 'table', 'rule': 'table-layout: fixed'},                        
                    ],
                    style_header={
                        'backgroundColor': 'rgb(30, 30, 30)',
                        'color': 'white',
                        'font-family': 'sans-serif',
                        'text-align': 'center'
                    },
                    style_data={
                        'width': '100%',
                        'backgroundColor': 'rgb(50, 50, 50)',
                        'color': 'white',
                        'font-family': 'sans-serif',
                    },
                    style_cell={
                        'textOverflow': 'ellipsis',
                        'overflow': 'hidden',
                        'backgroundColor': 'rgb(30, 30, 30)',
                        'color': 'white',
                        'font-family': 'sans-serif',
                        'text-align': 'center'
                    },
                    style_cell_conditional=[
                        {'if': {'column_id': 'Artist'},
                        'width': '50%'},
                        {'if': {'column_id': 'Album'},
                        'width': '50%'},
                    ],
                ),       
        ],className="text-white w-full h-full")
     else:
        return html.Div([
            html.H1("All albums have Genre/Style Assigned",className="text-white font-bold mt-2"),  
        ],className="flex")


def avg_style_table():
    return html.Div([
        dash_table.DataTable(
                id='datatable-avg-style',
                columns=[
                    {"name": i, "id": i} for i in avg_style_df.columns
                ],
                data=avg_style_df.to_dict('records'),          
                page_size=4,
                sort_action="native",
                sort_mode="multi",
                cell_selectable=False,
                css=[ 
                    {'selector': 'table', 'rule': 'table-layout: fixed'}, 
                ],
                style_header={
                    'backgroundColor': 'rgb(30, 30, 30)',
                    'color': 'white',
                    'font-family': 'sans-serif',
                    'text-align': 'center'
                },
                style_data={
                    'width': '100%',
                    'backgroundColor': 'rgb(50, 50, 50)',
                    'color': 'white',
                    'font-family': 'sans-serif',
                },
                style_cell={
                    'textOverflow': 'ellipsis',
                    'overflow': 'hidden',
                    'backgroundColor': 'rgb(30, 30, 30)',
                    'color': 'white',
                    'font-family': 'sans-serif',
                    'text-align': 'center'
                },            
            ),       
    ],className="text-white w-full h-full")


def avg_genre_table():
    return html.Div([
        dash_table.DataTable(
                id='datatable-avg-genre',
                columns=[
                    {"name": i, "id": i} for i in avg_genre_df.columns
                ],
                data=avg_genre_df.to_dict('records'),          
                page_size=4,
                sort_action="native",
                sort_mode="multi",
                cell_selectable=False,
                css=[ 
                    {'selector': 'table', 'rule': 'table-layout: fixed'},                     
                ],
                style_header={
                    'backgroundColor': 'rgb(30, 30, 30)',
                    'color': 'white',
                    'font-family': 'sans-serif',
                    'text-align': 'center'
                },
                style_data={
                    'width': '100%',
                    'backgroundColor': 'rgb(50, 50, 50)',
                    'color': 'white',
                    'font-family': 'sans-serif',
                },
                style_cell={
                    'textOverflow': 'ellipsis',
                    'overflow': 'hidden',
                    'backgroundColor': 'rgb(30, 30, 30)',
                    'color': 'white',
                    'font-family': 'sans-serif',
                    'text-align': 'center'
                },            
            ),       
    ],className="text-white w-full h-full")



layout = html.Div([

        #col1
        html.Div([    
            #row1
            html.Div([
                html.H1("Average Style Rating",className="text-xl text-white font-bold mb-2"), 
                avg_style_table()
                                    
            ],className="flex flex-col h-[32.5%] p-4 w-full rounded-lg bg-gradient-to-tr from-gray-800 to-black"),

            html.Div([
                html.H1("Average Genre Rating",className="text-xl text-white font-bold mb-2"), 
                avg_genre_table()
                                    
            ],className="flex flex-col h-[32.5%] p-4 w-full rounded-lg bg-gradient-to-tr from-gray-800 to-black"),

            #row2
             html.Div([
                 html.H1("Albums without Genre/Style Assigned",className="text-xl text-white font-bold mb-2"),  
                 no_style_table()                                    
            ],className="flex flex-col h-[32.5%] p-4 w-full rounded-lg bg-gradient-to-tr from-gray-800 to-black"),               

        ], className="flex flex-col justify-between h-full w-1/3"),


        #col2
        html.Div([ 
            html.H1('Genres and Style Breakdown', className="text-2xl font-bold text-white"),
            genres_treemap()   
                    

        ], className="p-2 flex flex-col h-full w-[66%]  rounded-lg bg-gradient-to-tr from-gray-800 to-black"),



],className="flex flex-row justify-between w-full h-full p-4")
#bg-gradient-to-br from-red-800 to-blue 
