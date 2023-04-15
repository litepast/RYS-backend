import spotipy
import config
from spotipy.oauth2 import SpotifyClientCredentials

class Search():

    results = None

    def __init__(self):
        self.client_id = config.spotify_id
        self.client_secret = config.spotify_client_secret     
        self.auth_manager = SpotifyClientCredentials(client_id=self.client_id, client_secret=self.client_secret)
        self.sp=spotipy.Spotify(auth_manager=self.auth_manager)
    
    def search_album(self,search_string,type_search: bool):        
        if (type_search):
            self.string_search=search_string
        else:
            self.string_search='artist:'+search_string

        results_columns = ['name', 'artist', 'album_id', 'release_date', 'cover_url']        
        results_rows = { column: [] for column in results_columns} 
        
        results_albums = self.sp.search(q=self.string_search , type='album', limit=5, market='MX')
        if results_albums:
            albums = results_albums['albums']['items'] 
            for album in albums:
                results_rows['name'].append(album['name'])
                results_rows['artist'].append(album['artists'][0]['name']) 
                results_rows['album_id'].append(album['id']) 
                results_rows['release_date'].append(album['release_date']) 
                results_rows['cover_url'].append(album['images'][1]['url'])
            self.results = results_rows
        return self.results 
    
    def get_album_id(self,index):
            return self.results['album_id'][index]



        



