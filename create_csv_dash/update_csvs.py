import pandas as pd
from config import engine

def update_csvs():
    try:
        years_albums_q= """select art.name Artist, al.name Album, left(al.release_date,4) Year,
        left(release_date,4)-MOD(left(release_date,4),10) as Decade, ar.user_final_rating Rating, if(ar.user_final_rating is not null, 'Rated', 'Unrated') Rated
        from albums al left join album_ratings ar on al.id = ar.id_album left join artists art on al.artist_id = art.id"""
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
        avg_style_q= """  select style_name Style,  count(sa.id_album) `Albums Rated`, format(avg(user_final_rating),2) `Average Rating`
        from styles_by_album sa left join album_ratings ar on sa.id_album = ar.id_album
        where user_final_rating is not null and sa.style_name <> 'NOT_FOUND'
        group by style_name
        order by 2 desc, 3 desc; """
        avg_genre_q= """select genre_name Genre, count(ga.id_album) `Albums Rated`, format(avg(user_final_rating),2) `Average Rating`
        from genres_by_album ga left join album_ratings ar on ga.id_album = ar.id_album
        where user_final_rating is not null and ga.genre_name <> 'NOT_FOUND'
        group by genre_name 
        order by 2 desc, 3 desc;"""    
        total_albums_q="select count(id) as `Total Albums` from albums"
        total_rated_albums_q="select count(id_album) as `Albums Rated` from album_ratings where user_final_rating is not null;"
        total_stars_albums_q="select avg(user_final_rating) as `Average Album Rating` from album_ratings where user_final_rating is not null;"
        total_tracks_q="select count(id) as `Total Tracks` from tracks"
        total_rated_tracks_q="select count(id_track) as `Tracks Rated` from track_ratings where rating is not null;"
        total_stars_tracks_q="select avg(rating) as `Average Track Rating` from track_ratings where rating is not null;"
        ratings_albums_q="""select rv.Rating, ifnull(Count,0) Quantity from ratings_values rv left join
        (select user_final_rating as Rating, count(user_final_rating) as Count from album_ratings group by user_final_rating) ar
        on rv.Rating = ar.Rating order by 1 desc ;"""
        ratings_tracks_q="""select rv.Rating, ifnull(Count,0) Quantity from ratings_values rv left join
        (select rating as Rating, count(rating) as Count from track_ratings group by rating) tr
        on rv.Rating = tr.Rating order by 1 desc ;"""
        types_q="""select at.name Type, ifnull(t.count,0) Quantity from album_types at
        left join (select type_id, count(id) Count from albums group by type_id) t on at.id=t.type_id;"""
        activity_q="""select  al.name Album, art.name Artist, ar.user_final_rating Rating, ar.updated_date Date, al.cover_url Cover from album_ratings 
        ar left join albums al on ar.id_album = al.id 
        left join artists art on art.id = al.artist_id
        where ar.user_final_rating is not null 
        order by 4 desc limit 20;"""
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
    
        totalAbums_df=pd.read_sql(total_albums_q, engine)
        totalRatedAbums_df=pd.read_sql(total_rated_albums_q, engine)
        totalStarsAbums_df=pd.read_sql(total_stars_albums_q, engine)
        totalTracks_df=pd.read_sql(total_tracks_q, engine)
        totalRatedTracks_df=pd.read_sql(total_rated_tracks_q, engine)
        totalStarsTracks_df=pd.read_sql(total_stars_tracks_q, engine)
        ratingsalbum_df = pd.read_sql(ratings_albums_q, engine)
        ratingstrack_df = pd.read_sql(ratings_tracks_q, engine)
        types_df = pd.read_sql(types_q, engine)
        activity_df = pd.read_sql(activity_q, engine)
        avg_style_df = pd.read_sql(avg_style_q, engine)
        no_style_df = pd.read_sql(no_style_q, engine)
        styles_df = pd.read_sql(styles_q, engine)
        avg_genre_df = pd.read_sql(avg_genre_q, engine)
        yearsalbum_df = pd.read_sql(years_albums_q, engine)
        artists_df = pd.read_sql(artists_q, engine)
        tooltip_df = pd.read_sql(tooltip_q, engine)

        totalAbums_df.to_csv("./Data/ratings_dashboard/totalAbums.csv", header=True, index=False)
        totalRatedAbums_df.to_csv("./Data/ratings_dashboard/totalRatedAbums.csv", header=True, index=False)
        totalStarsAbums_df.to_csv("./Data/ratings_dashboard/totalStarsAbums.csv", header=True, index=False)
        totalTracks_df.to_csv("./Data/ratings_dashboard/totalTracks.csv", header=True, index=False)
        totalRatedTracks_df.to_csv("./Data/ratings_dashboard/totalRatedTracks.csv", header=True, index=False)
        totalStarsTracks_df.to_csv("./Data/ratings_dashboard/totalStarsTracks.csv", header=True, index=False)
        ratingsalbum_df.to_csv("./Data/ratings_dashboard/ratingsalbum.csv", header=True, index=False)
        ratingstrack_df.to_csv("./Data/ratings_dashboard/ratingstrack.csv", header=True, index=False)
        types_df.to_csv("./Data/ratings_dashboard/types.csv", header=True, index=False)
        activity_df.to_csv("./Data/ratings_dashboard/activity.csv", header=True, index=False)
        avg_style_df.to_csv("./Data/styles_dashboard/avg_style.csv", header=True, index=False)
        no_style_df.to_csv("./Data/styles_dashboard/no_style.csv", header=True, index=False)
        styles_df.to_csv("./Data/styles_dashboard/styles.csv", header=True, index=False)
        avg_genre_df.to_csv("./Data/styles_dashboard/avg_genre.csv", header=True, index=False)
        yearsalbum_df.to_csv("./Data/years_dashboard/yearsAbums.csv", header=True, index=False)
        artists_df.to_csv("./Data/artists_dashboard/artists.csv", header=True, index=False)
        tooltip_df.to_csv("./Data/artists_dashboard/tooltip.csv", header=True, index=False)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    update_csvs()