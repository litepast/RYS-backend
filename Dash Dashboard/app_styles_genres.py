from dash import Dash, html, dcc, dash_table
from config import engine
import plotly.express as px
import pandas as pd


styles_q= """
select 'Genres & Styles' Tag, g.name Genre, sa.style_name Style, concat(al.name,' by ',art.name, ' : ', ifnull(ars.user_final_rating,'Unrated')) Album, 1 Quantity from styles_by_album sa left join styles s on sa.style_name=s.name left join genres g on s.genre_id = g.id left join albums al on al.id=sa.id_album
left join artists art on art.id = al.artist_id
left join album_ratings ars on al.id = ars.id_album
where sa.style_name <> 'NOT_FOUND' order by 1; 
"""
styles_df = pd.read_sql(styles_q, engine)

no_style_q= """
select al.name Album, art.name Artist from
(select id_album from styles_by_album where style_name = 'NOT_FOUND'
union
select id_album from genres_by_album where genre_name = 'NOT_FOUND') A
left join albums al on A.id_album = al.id
left join artists art on al.artist_id=art.id
"""
no_style_df = pd.read_sql(no_style_q, engine)


avg_style_q= """
select style_name Style,  count(sa.id_album) `Albums Rated`, format(avg(user_final_rating),2) `Average Rating`  from styles_by_album sa left join album_ratings ar on sa.id_album = ar.id_album
where user_final_rating is not null and sa.style_name <> 'NOT_FOUND'
group by style_name
order by 2 desc, 3 desc;
"""

avg_style_df = pd.read_sql(avg_style_q, engine)


avg_genre_q= """
select genre_name Genre, count(ga.id_album) `Albums Rated`, format(avg(user_final_rating),2) `Average Rating`  from genres_by_album ga left join album_ratings ar on ga.id_album = ar.id_album
where user_final_rating is not null and ga.genre_name <> 'NOT_FOUND'
group by genre_name 
order by 2 desc, 3 desc;
"""

avg_genre_df = pd.read_sql(avg_genre_q, engine)

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
