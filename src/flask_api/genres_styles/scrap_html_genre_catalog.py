from bs4 import BeautifulSoup

##Desde el archivo que se obtiene en https://web.archive.org/web/20220810095106/https://blog.discogs.com/en/genres-and-styles/
# ese pagina la guardo en esta carpeta como genres_styles  
def webscrap_genres_and_styles():
    try:
        genres_html="./src/flask_api/genres_styles/genres_styles.htm"
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


if __name__ == "__main__":
       webscrap_genres_and_styles()




  






