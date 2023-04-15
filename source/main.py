import os
from search_album import Search
from insert_album import Album 
import pandas as pd

def main():
     os.system("cls")
     type_search = bool(input('1 por Album / 0 por Artista: '))
     string_search = input('Tu busqueda: ')
     search = Search()
     albums_result=search.search_album(string_search,type_search)
     if albums_result:
          results_df = pd.DataFrame(albums_result)
          results_df = results_df[['name', 'artist', 'release_date']]
          print(results_df)
          result_index=int(input('Que album quieres guardar por numero?: '))   
          album_id = search.get_album_id(result_index) 
          print(album_id)
          insert_album = Album(album_id)
          insert_album.insert_album_data()
     else:
          print('No hay resultados')
   
     print("Fin de Programa")
     return

if __name__ == "__main__":
     main()

  # #69 love songs
     # #insert_album=InsertAlbum('2GuROKcqyHdpIDcgxml1C7')

     # #ok computer
     # #insert_album=InsertAlbum('6dVIqQ8qmQ5GBnJ9shOYGE')

     # #compilacion
     # insert_album=Album('0RPeS6tlJfJt1GQ1XilhkH')


# #Magnetic fields
# result_album_id='2GuROKcqyHdpIDcgxml1C7'
# result_artist_id='6RWjTQqILL7a1tQ0VapyLK'

# #gybe
# result_artist_id='4svpOyfmQKuWpHLjgy4cdK'
# result_album_id='2tA6VFMIQuSF3KpXsrulw9'

#OK computer
#6dVIqQ8qmQ5GBnJ9shOYGE

#super copilacion
# 0RPeS6tlJfJt1GQ1XilhkH



 


