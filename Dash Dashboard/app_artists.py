from dash import html, dash_table
from config import engine
import pandas as pd
import textwrap

artists_q="""select A.id, A.Artist, 
ifnull(B.`Rated Albums`,0) `Rated Albums`,
ifnull(C.`Unrated Albums`,0) `Unrated Albums`,
ifnull(D.`Rated Tracks`,0) `Rated Tracks`,
ifnull(E.`Unrated Tracks`,0) `Unrated Tracks`,
ifnull(F.`Goated Tracks`,0) `Goated Tracks`,
ifnull(G.`Average Track Rating`,'-') `Average Track Rating`, 
ifnull(H.`Average Album Rating`,'-') `Average Album Rating`
from 
(select art.id id , art.name Artist from artists art) A 
left join
(select al.artist_id id, count(al.artist_id) `Rated Albums` from  albums al left outer join album_ratings ar  on ar.id_album = al.id
where ar.user_final_rating is not null group by al.artist_id)  B 
on A.id = B.id
left join
(select al.artist_id id, count(al.artist_id) `Unrated Albums` from  albums al left outer join album_ratings ar  on ar.id_album = al.id
where ar.user_final_rating is null group by al.artist_id) C 
on A.id = C.id
left join
(select t.artist_id id, count(tr.rating) `Rated Tracks` from tracks t left join track_ratings tr on t.id = tr.id_track
where tr.rating is not null group by t.artist_id) D
on A.id = D.id
left join
(select t.artist_id id, count(ifnull(tr.rating,1)) `Unrated Tracks` from tracks t left join track_ratings tr on t.id = tr.id_track
where tr.rating is null group by t.artist_id) E
on A.id = E.id
left join
(select t.artist_id id, count(tr.goated) `Goated Tracks` from tracks t left join track_ratings tr on t.id = tr.id_track
where tr.goated = 1 group by t.artist_id) F
on A.id = F.id
left join
(select t.artist_id id, format(avg(tr.rating),2) `Average Track Rating` from tracks t left join track_ratings tr on t.id = tr.id_track
where tr.rating is not null group by t.artist_id) G
on A.id = G.id 
left join
(select art.id id, round(avg(ar.user_final_rating),2) `Average Album rating` from 
albums al left outer join album_ratings ar  on ar.id_album = al.id left join  
artists art on al.artist_id = art.id where ar.user_final_rating is not null group by al.artist_id) H
on A.id = H.id
order by 3 desc, 9 desc, 8 desc;"""

tooltip_q="""select al.artist_id,  left(al.release_date,4) Year, al.name Album, ifnull(ar.user_final_rating,'Unrated')  Rating  from albums al left join album_ratings ar on al.id = ar.id_album
order by 1, 2 asc"""

artists_df = pd.read_sql(artists_q, engine)
tooltip_df = pd.read_sql(tooltip_q, engine)


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

