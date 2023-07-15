import plotly.express as px
import pandas as pd
from config import engine

def save_queries_to_csv():

    styles_q= """select 'Genres & Styles' Tag, g.name Genre, sa.style_name Style, concat(al.name,' by ',art.name, ' : ', ifnull(ars.user_final_rating,'Unrated')) Album, 1 Quantity from styles_by_album sa left join styles s on sa.style_name=s.name left join genres g on s.genre_id = g.id left join albums al on al.id=sa.id_album
    left join artists art on art.id = al.artist_id
    left join album_ratings ars on al.id = ars.id_album
    where sa.style_name <> 'NOT_FOUND' order by 1;""" 
    no_style_q= """ select al.name Album, art.name Artist from
    (select id_album from styles_by_album where style_name = 'NOT_FOUND'
    union
    select id_album from genres_by_album where genre_name = 'NOT_FOUND') A
    left join albums al on A.id_album = al.id
    left join artists art on al.artist_id=art.id """
    avg_style_q= """  select style_name Style,  count(sa.id_album) `Albums Rated`, format(avg(user_final_rating),2) `Average Rating`  from styles_by_album sa left join album_ratings ar on sa.id_album = ar.id_album
    where user_final_rating is not null and sa.style_name <> 'NOT_FOUND'
    group by style_name
    order by 2 desc, 3 desc; """
    avg_genre_q= """select genre_name Genre, count(ga.id_album) `Albums Rated`, format(avg(user_final_rating),2) `Average Rating`  from genres_by_album ga left join album_ratings ar on ga.id_album = ar.id_album
    where user_final_rating is not null and ga.genre_name <> 'NOT_FOUND'
    group by genre_name 
    order by 2 desc, 3 desc;"""

    avg_style_df = pd.read_sql(avg_style_q, engine)
    no_style_df = pd.read_sql(no_style_q, engine)
    styles_df = pd.read_sql(styles_q, engine)
    avg_genre_df = pd.read_sql(avg_genre_q, engine)

    avg_style_df.to_csv("./Data/styles_dashboard/avg_style.csv", header=True, index=False)
    no_style_df.to_csv("./Data/styles_dashboard/no_style.csv", header=True, index=False)
    styles_df.to_csv("./Data/styles_dashboard/styles.csv", header=True, index=False)
    avg_genre_df.to_csv("./Data/styles_dashboard/avg_genre.csv", header=True, index=False)

save_queries_to_csv()
















