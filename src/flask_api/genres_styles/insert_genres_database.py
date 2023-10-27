import pandas as pd
from sqlalchemy.exc import OperationalError
from scrap_html_genre_catalog import webscrap_genres_and_styles
import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
grandparent = os.path.dirname(parent)
sys.path.append(grandparent)
import config


def insert_genres_database():    
    engine = config.engine
    try:        
        genres_dict=webscrap_genres_and_styles() 
        genres_list=list(genres_dict.keys())
        df_genres = pd.DataFrame(genres_list, columns=['genre_name'])
        df_genres.insert(0, 'genre_id', df_genres.reset_index().index+1)

        styles_list = [(key, item) for key in genres_dict.keys() for item in genres_dict[key]]
        df_styles =pd.DataFrame(styles_list,columns=['genre_name', 'style_name'])
        df_styles.insert(0, 'style_id', df_styles.reset_index().index+1)

        df_styles=pd.merge(df_styles, df_genres, how='left', on = 'genre_name')
        df_styles=df_styles[['style_id','genre_id','style_name']]       

        df_genres = df_genres.rename(columns={'genre_id': 'id', 'genre_name' : 'name'})
        df_styles = df_styles.rename(columns={'style_id': 'id', 'style_name' : 'name'})

        print(df_genres)

        df_genres.to_sql(name='genres', con=engine, if_exists='append', index=False)
        df_styles.to_sql(name='styles', con=engine, if_exists='append', index=False)
    except OperationalError as e:
      print(f"Connection failed: {e}")
    finally:
       engine.dispose()

if __name__ == "__main__":
    insert_genres_database()









