import plotly.express as px
import pandas as pd
from config import engine

def save_queries_to_csv():
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

    artists_df.to_csv("./Data/artists_dashboard/artists.csv", header=True, index=False)
    tooltip_df.to_csv("./Data/artists_dashboard/tooltip.csv", header=True, index=False)
        

save_queries_to_csv()
















