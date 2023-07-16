import plotly.express as px
import pandas as pd
from config import engine

def save_queries_to_csv():
    
    years_albums_q= """select art.name Artist, al.name Album, left(al.release_date,4) Year,
    left(release_date,4)-MOD(left(release_date,4),10) as Decade, ar.user_final_rating Rating, if(ar.user_final_rating is not null, 'Rated', 'Unrated') Rated
    from albums al left join album_ratings ar on al.id = ar.id_album left join artists art on al.artist_id = art.id"""


    yearsalbum_df = pd.read_sql(years_albums_q, engine)

    yearsalbum_df.to_csv("./Data/years_dashboard/yearsAbums.csv", header=True, index=False)

    

save_queries_to_csv()
















