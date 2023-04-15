import os
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from GetFromDiscogs import GetFromDiscogs

os.system("cls")
#crea conexion a mysql
#engine = create_engine("mysql+mysqlconnector://root:Adults2137224!@localhost:3306/rys")

#try:
    #Obtiene el distionary del Scrapeo
genres_dict=GetFromDiscogs.GetGenresStyles()

#Crea el catalogo de Genres, crea un df apartir de los Genres
#Despues insert una columna con el id, para que inice desde 1
genres_list=list(genres_dict.keys())
df_genres = pd.DataFrame(genres_list, columns=['genre_name'])
df_genres.insert(0, 'genre_id', df_genres.reset_index().index+1)

#Crea el catalogo de Styles, pasa todos los pares de Genres-Styles a una lista de tuples
#Despues de acuerdo al Genre, le agrega el Id con el catalogo de arriba
#Y reordena columnas
styles_list = [(key, item) for key in genres_dict.keys() for item in genres_dict[key]]
df_styles =pd.DataFrame(styles_list,columns=['genre_name', 'style_name'])
df_styles.insert(0, 'style_id', df_styles.reset_index().index+1)
df_styles=pd.merge(df_styles, df_genres, how='left', on = 'genre_name')
df_styles=df_styles[['style_id','genre_id','style_name']]

#renombrar columnas para matchear con mysql
df_genres = df_genres.rename(columns={'genre_id': 'id', 'genre_name' : 'name'})
df_styles = df_styles.rename(columns={'style_id': 'id', 'style_name' : 'name'})

print(df_genres)
print(df_styles)



# df_all = pd.concat([df_genres,df_styles.drop('genre_id',axis=1)])
# print(df_all)


#insert dataframe en sql
# df_genres.to_sql(name='genres', con=engine, if_exists='append', index=False)
# df_styles.to_sql(name='styles', con=engine, if_exists='append', index=False)
print("you did it!?")    
#except OperationalError as e:
#   print(f"Connection failed: {e}")
#finally:
#    engine.dispose()









