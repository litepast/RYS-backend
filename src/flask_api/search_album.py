import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
import config
from spotipy import SpotifyException

class Search():

    def __init__(self):
       self.sp = config.sp
    
    def search_album(self,type_search,search_string):
        try:                
            results = []
            # tipo 0 album names
            if (not type_search):
                self.string_search=search_string
            else:
            # tipo 0 album artist
                self.string_search='artist:'+search_string


            print('lo que se busca: ',self.string_search)
            results_columns = ['name', 'artist', 'album_id', 'release_date', 'cover_url']            
            results_albums = self.sp.search(q=self.string_search , type='album', limit=50, market="MX")
            if results_albums:
                albums = results_albums['albums']['items'] 
                for album in albums:
                    results_rows = { column: None for column in results_columns} 
                    results_rows['name']=album['name']
                    results_rows['artist']=album['artists'][0]['name']
                    results_rows['album_id'] = album['id']
                    results_rows['release_date'] = album['release_date']
                    results_rows['cover_url'] = album['images'][1]['url']
                    results.append(results_rows)
                self.results=results            
        except SpotifyException:
            self.results = []
        except Exception:
            self.results = []
        finally:
            return self.results
    
    def get_album_id(self,index):
            return self.results['album_id'][index]



        



