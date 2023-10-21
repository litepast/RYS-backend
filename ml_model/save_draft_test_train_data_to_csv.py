from config import engine
from sqlalchemy import text
from sqlalchemy.orm import Session
import pandas as pd

with Session(engine) as session:
        session.begin()
        try:
            q="""select a.name album, t.name song from tracks t left join albums a on t.album_id = a.id
            order by a.name, t.overall_number"""

            test_df=pd.read_sql(q, engine)
            test_dict = test_df.groupby('album')['song'].apply(list).to_dict()

            title=[]
            type=[]
            for album in test_dict:
                 title.append(album)
                 type.append("album")
                 for song in test_dict[album]:
                      title.append(song)
                      type.append("song")
                 
            test_df_to_save = pd.DataFrame({'type': type, 'title': title})
            test_df_to_save.to_csv("./ml_model/first_data.csv", header=True, index=False)


        except Exception as e:
            print(e)        