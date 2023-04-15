from bs4 import BeautifulSoup
import os
os.system("cls")

# Vamos a intentar usar la relacion de genres y styles de Discogs para
# Crear nuestro catalos, para poder asignarlos a los albums de spotify
# Dado que los genres de Spotify estan muy pobres
# Relacion la sacamos de un archivo local dado que la API de Discogs no tiene la info
# y la web de Discogs no permite scrapear

class GetFromDiscogs():

    def __init__(self) -> None:
        pass
    
    def GetGenresStyles():
        try:
        #se abre y se convierte a un bs el html
            with open('C:/Python/Genres_Styles/Genres_and_Styles_Discogs.html', 'r') as f:
                html = f.read()
                soup = BeautifulSoup(html, 'html.parser')
                all_tags = soup.find_all()  
                print('INICIO')

            #Los tags estan al mismo nivel,  los pasamos en orden a una lista de bs.tags
            tags =  [tag for tag in all_tags if tag.name=='h3' or  tag.name=='span' and tag.has_attr('class') and tag['class']==['gsl-artist']]

            #si son h3 son los genres padres y lo de abajo si son span son sus hijos
            genres_dict={}
            i=0
            for tag in tags:
                if(tag.name=='h3'):
                    temp_list=[]
                    temp_key=tag.text
                    if temp_key not in genres_dict:
                        genres_dict[temp_key]=temp_list
                if(tag.name=='span'):
                    i=i+1
                    temp_list.append(tag.text)
                    genres_dict[temp_key]=temp_list           
            return genres_dict
            
            
        except Exception as e:
            print(f"An error occurred: {e}")
            return e
        finally:
            # cerrar archivo
            if 'f' in locals() and not f.closed:
                f.close()    




  






