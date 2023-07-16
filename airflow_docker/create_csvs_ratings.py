import plotly.express as px
import pandas as pd
from config import engine

def save_queries_to_csv():
    #Ratings CSV
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
    activity_q="""select  al.name Album, art.name Artist, ar.user_final_rating Rating, ar.updated_date Date, al.cover_url Cover from album_ratings ar left join albums al on ar.id_album = al.id 
    left join artists art on art.id = al.artist_id
    where ar.user_final_rating is not null 
    order by 4 desc limit 20;"""

    #given the strings above, execute the queries and save dataframes to csv files
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

    #now save the dataframes to csv files
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
    

save_queries_to_csv()
















