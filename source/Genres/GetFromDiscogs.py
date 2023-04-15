from bs4 import BeautifulSoup
import os
from config import genres_html
os.system("cls")

class GetFromDiscogs():

    def __init__(self) -> None:
        pass
    
    def GetGenresStyles():
        try:
            with open(genres_html, 'r') as f:
                html = f.read()
                soup = BeautifulSoup(html, 'html.parser')
                all_tags = soup.find_all() 
                
            tags =  [tag for tag in all_tags if tag.name=='h3' or  tag.name=='span' and tag.has_attr('class') and tag['class']==['gsl-artist']]

            genres_dict={}
            for tag in tags:
                if(tag.name=='h3'):
                    temp_list=[]
                    temp_key=tag.text
                    if temp_key not in genres_dict:
                        genres_dict[temp_key]=temp_list
                if(tag.name=='span'):
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




  






