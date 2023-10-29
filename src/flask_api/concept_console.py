import os
from search_album import Search
from insert_album import Album 
import pandas as pd

# proof on concept, doing a album search on spotify only on console commands
# it prints the results of the search, on a pandas df, then given the row, it can save the album's data on the db
# this was the first file worked at the beginning of the project, before any frontend work began
# inputs intructions done in spanish :P

def main():
     while True:
          os.system("cls")           
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
          if albums_result:
               results_df = pd.DataFrame(albums_result)
               results_df = results_df[['name', 'artist', 'release_date']]
               print(results_df)
               while True:
                    try:
                         result_index=int(input('Que album quieres guardar por numero?: '))                         
                         album_id = albums_result[result_index]['album_id']           
                         insert_album = Album(album_id)
                         status, msg =insert_album.insert_album_data()
                         print(status,' ',msg)
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


if __name__ == "__main__":
     main()






 


