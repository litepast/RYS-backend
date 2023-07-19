import pandas as pd
from config import mysql_connection as engine

tooltip_q="""select al.artist_id,  left(al.release_date,4) Year, al.name Album, ifnull(ar.user_final_rating,'Unrated')  Rating  from albums al left join album_ratings ar on al.id = ar.id_album
order by 1, 2 asc"""


tooltip_df = pd.read_sql(tooltip_q, engine)


def create_tooltip():
    id='053q0ukIDRgzwTr4vNSwab'
    artist='Grimes'
    df = tooltip_df[tooltip_df['artist_id'] == id]
    df = df[['Year', 'Album', 'Rating']]
    lines=[]
    for row in df.to_dict('records'):
        line=[]
        for value in row.values():
            line.append(value)
        lines.append(line)    
    max_length = max(len(line[1]) for line in lines)    
    tooltip = "Your Albums by {}".format(artist)+"\n{:4} | {:{length}} | {:8}".format("Year", "Album", "Your Rating",length=max_length)
    formatted_rows = ["\n{:4} | {:{length}} | {:8}".format(row[0], row[1], row[2], length=max_length) for row in lines] 
    for formatted_row in formatted_rows:
        tooltip=tooltip+formatted_row    
    print(tooltip)


create_tooltip()









# from insert_album import Album

# a = Album('29exN2kWgZTxFh687nwi2r')
# msg, st = a.insert_album_data()
# print(msg, st)

# import models
# from sqlalchemy import text
# from sqlalchemy.orm import Session
# from get_bg_color import best_color

# def init_all_color(): 
#     with Session(models.engine) as session:
#         session.begin()
#         try:            
#             albums_query = "select id, cover_url from albums where cover_color_to is null"
#             albums = session.execute(text(albums_query) )
#             for i, album in enumerate(albums):
#                 print(album[0])
#                 print(album[1])
#                 color, color_to = best_color(album[1])                           
#                 print(color, ' ',color_to,' ', album[0])
#                 update_query = "update albums set cover_color_to = '{}' where id = '{}'".format(color_to, album[0])
#                 print(i)
                
#                 print(update_query)
#                 session.execute(text(update_query))
#         except Exception as e:
#             print(e)
#             session.rollback()        
#         else:
#             print('commited')
#             session.commit()


# init_all_color()
        