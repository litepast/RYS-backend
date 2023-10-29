import pandas as pd
import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from config import engine

#script creats csvs files used in the tableau dashboard datasource

def update_csvs():  
    try:        
        albums_q = """select 
                a.id Album_id, a.name Album, art.name Album_Artist, at.name Type, left(a.release_date,4) as Year, left(a.release_date,4)-MOD(left(a.release_date,4),10) as Decade, 
                ar.suggested_rating_final Suggested_Rating, ar.user_final_rating Rating, ar.updated_date Updated_date 
                from albums a left join album_ratings ar on a.id= ar.id_album
                left join artists art on art.id = a.artist_id
                left join album_types at on at.id=a.type_id;"""

        tracks_q = """select a.id Album_id, a.name Album, tx.Name Track, art.name Artist_Track, 
                tx.overall_number Number,
                tr.goated Goated, tr.rating Rating, tx.duration_ms Duration
                from tracks tx left join albums a on tx.album_id=a.id
                left join track_ratings tr on tx.id = tr.id_track
                left join artists art on tx.artist_id = art.id
                order by 1,5;
                """
        
        artists_q="""select art.name Artist, art.popularity Popularity from artists art where exists
                (select artist_id from albums al where al.artist_id=art.id);
                """
        styles_q="""
               select ga.genre_name Genre, sa.style_name Style, al.id Album_id, al.name Album from albums al
                left join genres_by_album ga on al.id=ga.id_album
                left join styles_by_album sa on sa.id_album=al.id
                where ga.genre_name <> 'NOT_FOUND' or
                sa.style_name <> 'NOT_FOUND'"""
    
        albums_df = pd.read_sql(albums_q, engine)
        tracks_df = pd.read_sql(tracks_q, engine)
        artists_df = pd.read_sql(artists_q,  engine)
        styles_df = pd.read_sql(styles_q,  engine)  
 
        albums_df.to_csv("./Data/tableau_csvs/albums.csv", header=True, index=False)
        tracks_df.to_csv("./Data/tableau_csvs/tracks.csv", header=True, index=False)
        artists_df.to_csv("./Data/tableau_csvs/artists.csv", header=True, index=False)
        styles_df.to_csv("./Data/tableau_csvs/styles.csv", header=True, index=False)       
 
    except Exception as e:
        print(e)

if __name__ == "__main__":
       update_csvs()