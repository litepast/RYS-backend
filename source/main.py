import os
from search_album import Search
from insert_album import Album 
import pandas as pd

def main():
     os.system("cls")     
     while True:
          while True:
               try:
                    type_search = int(input('1 por Album / 0 por Artista: '))
                    break
               except ValueError:
                    print('Dato no valido')
          while True:
               try:
                    string_search = input('Tu busqueda: ')
                    break
               except ValueError:
                    print('Dato no valido')
          search = Search()
          albums_result=search.search_album(string_search,type_search)
          if albums_result['name']:
               results_df = pd.DataFrame(albums_result)
               results_df = results_df[['name', 'artist', 'release_date']]
               print(results_df)
               while True:
                    try:
                         result_index=int(input('Que album quieres guardar por numero?: '))
                         album_id = search.get_album_id(result_index)           
                         insert_album = Album(album_id)
                         insert_album.insert_album_data()
                         break
                    except ValueError:
                         print('Dato no es numero')    
                    except IndexError:
                         print('Indice no existe')  
          else:
               print('No hay resultados')          
          while True:
               try:
                    exit=input('Continuar? Y/N: ')
                    break
               except ValueError:
                    print('Dato no valido')
          if exit != 'Y':
               break
     print("Fin de Programa")
     return

def main2():     
     # #69 love songs
     #insert_album = Album('2GuROKcqyHdpIDcgxml1C7')
     # #ok computer
     insert_album = Album('6dVIqQ8qmQ5GBnJ9shOYGE')
     # #compilacion
     #insert_album = Album('0RPeS6tlJfJt1GQ1XilhkH')
     # new kanada
     #insert_album = Album('2tA6VFMIQuSF3KpXsrulw9')
     insert_album.insert_album_data()
     return

if __name__ == "__main__":
     main2()

     




 


