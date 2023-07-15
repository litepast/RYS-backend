from dash import html, dash_table
import pandas as pd
import textwrap

artists_df = pd.read_csv("./Data/artists_dashboard/artists.csv")
tooltip_df = pd.read_csv("./Data/artists_dashboard/tooltip.csv")



def artist_table():
     return html.Div([
          
          html.H1("Artist Breakdown",className="text-xl text-white font-bold mb-3"),
          
          dash_table.DataTable(
                id='datatable-interactivity-3',
                columns=[
                    {"name": i, "id": i} for i in artists_df.columns
                ],
                data=artists_df.to_dict('records'),          
                page_size=24,
                sort_action="native",
                sort_mode="multi",
                cell_selectable=False,
                css=[ 
                    {'selector': 'table', 'rule': 'table-layout: fixed'}, 
                    {'selector': '.dash-table-tooltip','rule': 'background-color: rgb(50, 50, 50); color: white;  width:auto !important; max-width:800px !important;’,'}
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
                    'width': '20%'},
                    {'if': {'column_id': 'id'},
                    'width': '0%'},
                ],
            
                tooltip_data=[
                    {
                        column: {'value': create_tooltip(artists_df.loc[i, 'id'],artists_df.loc[i, 'Artist'],artists_df.loc[i, 'Rated Albums'],artists_df.loc[i, 'Unrated Albums']),
                                  'type': 'markdown'}
                        for column in artists_df.columns
                    } 
                    for i in range(len(artists_df))
                ],
                tooltip_duration=None,
                tooltip_delay=0,

            ),       
    ],className="flex text-white flex-col items-center rounded-lg w-full h-full bg-gradient-to-tl from-gray-800 to-black")



def create_tooltip(id,artist,rated,unrated):
    total = rated + unrated
    df = tooltip_df[tooltip_df['artist_id'] == id]
    df = df[['Year', 'Album', 'Rating']]
    if len(df) > 0:
        lines=[]
        for row in df.to_dict('records'):
            line=[]
            for value in row.values():
                line.append(value)
            lines.append(line)    
        max_length = max(len(line[1]) for line in lines)
        nalbums = 'Albums' if total > 1 else 'Album'
        tooltip = """Your {} {} by ***{}*** \n""".format(total,nalbums,artist)
        
        formatted_rows = [""" \n{:4} | {:{length}} : {:12}""".format(row[0], row[1], 'Unrated' if row[2]=='Unrated' else str(row[2])+' Stars', length=max_length) for row in lines] 
        for formatted_row in formatted_rows:
            tooltip=tooltip+formatted_row    
        return textwrap.dedent(tooltip)
    else:
        return """No Albums by {}, 
                only features""".format(artist)



layout = html.Div([
        artist_table(),
],className="flex flex-col w-full h-full p-4")

