import pandas as pd
import config
import datetime
import time
from sqlalchemy import create_engine, text
from spotipy import SpotifyException
from discogs_client.exceptions import HTTPError as DiscogsException


class Album():
    user_id = 1 
    #Data for each table at the begining as None
    albums_data = None
    tracks_data = None
    artists_data =  None
    genres_data = None
    styles_data = None
    album_ratings_data = None
    track_ratings_data = None
    # variables to pass through fetch functions    
    album_artist = None
    album_name = None
    no_tracks = None
    id_tracks = None
    all_artists = None
    all_success = True


    def __init__(self,album_id):
        self.album_id = album_id
        self.sp = config.sp
        self.d = config.d


    def fetch_albums_data(self):
        try: 
            types_dict = {'album':1 , 'single':2, 'compilation':3 }
            album = self.sp.album(self.album_id)    
            albums_columns = ['id', 'artist_id', 'type_id', 'name', 'release_date','release_precision', 'total_tracks', 'cover_url']        
            albums_rows = { column: [] for column in albums_columns}       
            albums_rows['id'].append(album['id'])
            albums_rows['artist_id'].append(album['artists'][0]['id'])
            albums_rows['type_id'].append(types_dict[album['album_type']])
            albums_rows['name'].append(album['name'])
            albums_rows['release_date'].append(album['release_date'])
            albums_rows['release_precision'].append(album['release_date_precision'])
            albums_rows['total_tracks'].append(album['total_tracks']) 
            albums_rows['cover_url'].append(album['images'][1]['url']) 
            self.no_tracks =  albums_rows['total_tracks'][0]
            self.album_artist = album['artists'][0]['name']            
            self.album_name = album['name']
            self.albums_data = albums_rows
        except SpotifyException:
            self.all_success = False
        except Exception:
            self.all_success = False


    def fetch_tracks(self): 
        def fetch_tracks_onecall():
            tracks_result = self.sp.album_tracks(self.album_id)        
            tracks_result = tracks_result['items']
            tracks_columns = [ 'id', 'album_id', 'artist_id', 'disc_number','track_number','overall_number','name','duration']
            tracks_rows = { column: [] for column in tracks_columns} 
            for i,track in enumerate(tracks_result, 1): 
                tracks_rows['id'].append(track['id'])
                tracks_rows['album_id'].append(self.album_id)
                tracks_rows['artist_id'].append(track['artists'][0]['id'])
                tracks_rows['disc_number'].append(track['disc_number'])
                tracks_rows['track_number'].append(track['track_number'])
                tracks_rows['overall_number'].append(i)
                tracks_rows['name'].append(track['name'])
                tracks_rows['duration'].append(track['duration_ms'])           
            return tracks_rows                 
        def fetch_tracks_several(limits):
            tracks_columns = [ 'id', 'album_id', 'artist_id', 'disc_number','track_number','overall_number','name','duration']
            tracks_rows = { column: [] for column in tracks_columns}     
            for n,limit in enumerate(limits):          
                tracks_result = self.sp.album_tracks(self.album_id,limit=limit,offset=(n*50))
                tracks_result = tracks_result['items']
                for i,track in enumerate(tracks_result, 1): 
                    tracks_rows['id'].append(track['id'])
                    tracks_rows['album_id'].append(self.album_id)
                    tracks_rows['artist_id'].append(track['artists'][0]['id'])
                    tracks_rows['disc_number'].append(track['disc_number'])
                    tracks_rows['track_number'].append(track['track_number'])
                    tracks_rows['overall_number'].append((n*50)+i)
                    tracks_rows['name'].append(track['name'])
                    tracks_rows['duration'].append(track['duration_ms'])
            return tracks_rows        
        def limits_per_call():
            n = self.no_tracks // 50
            mod = self.no_tracks % 50 
            limits = [50]*n
            if mod > 0:
                limits.append(mod)
            return limits            
        try:
            if self.no_tracks is not None and self.no_tracks <= 50:         
                self.tracks_data = fetch_tracks_onecall()
                self.id_tracks = self.tracks_data['id']
            else:            
                self.tracks_data = fetch_tracks_several(limits_per_call())
                self.id_tracks = self.tracks_data['id']
        except SpotifyException:
            self.all_success = False
        except IndexError:
            self.all_success = False
        except Exception:
            self.all_success = False


    def fetch_artists_data(self):
        def combine_artists():
            if (self.albums_data and self.tracks_data):
                self.all_artists = list(set((self.albums_data['artist_id']+self.tracks_data['artist_id']))) 
                return True
            else:
                return False
        def slice_artists(all_artists):
            return [all_artists[index : index + 50] for index in range(0, len(all_artists), 50)]
        try:
            if(combine_artists()):
                artists_columns = [ 'id', 'name','popularity']
                artists_rows = { column: [] for column in artists_columns} 
                artists=slice_artists(self.all_artists)       
                for slice in artists:            
                    artists_results=self.sp.artists(slice)
                    artists_results=artists_results['artists']
                    for artist in artists_results:
                        artists_rows['id'].append(artist['id'])
                        artists_rows['name'].append(artist['name'])
                        artists_rows['popularity'].append(artist['popularity'])
                self.artists_data = artists_rows
            else: 
                self.all_success = False 
        except SpotifyException:
            self.all_success = False 
        except Exception:
            self.all_success = False   


    def fetch_album_ratings(self):
        try:
            aratings_columns = [ 'id_user', 'id_album','simple_avg_rating','more_than_nine_rating','weight_rating','suggested_rating_a','suggested_rating_b','user_final_rating','created_date','updated_date']
            aratings_rows = { column: [] for column in aratings_columns} 
            dt = datetime.datetime.now()              
            aratings_rows['id_user'].append(1) #cambiar usuario cuando se implemente login
            aratings_rows['id_album'].append(self.album_id)
            aratings_rows['simple_avg_rating'].append(None)
            aratings_rows['more_than_nine_rating'].append(None)
            aratings_rows['weight_rating'].append(1) 
            aratings_rows['suggested_rating_a'].append(None)
            aratings_rows['suggested_rating_b'].append(None)
            aratings_rows['user_final_rating'].append(None)
            aratings_rows['created_date'].append(dt) 
            aratings_rows['updated_date'].append(dt)  
            self.album_ratings_data = aratings_rows
        except Exception:
            self.all_success = False 
    

    def fetch_track_ratings(self):
        try:
            tratings_columns = [ 'id_user', 'id_track','rating','goated','included']
            tratings_rows = { column: [] for column in tratings_columns} 
            for track in self.id_tracks:
                tratings_rows['id_user'].append(1) #cambiar usuario cuando se implemente login
                tratings_rows['id_track'].append(track)
                tratings_rows['rating'].append(0)
                tratings_rows['goated'].append(0)
                tratings_rows['included'].append(1)
            self.track_ratings_data =  tratings_rows
        except Exception:
            self.all_success = False 


    def fetch_genres_and_styles(self):
        try:
            genres_columns = [ 'id_album', 'genre_name']
            genres_rows = { column: [] for column in genres_columns}
            styles_columns = [ 'id_album', 'style_name']
            styles_rows = { column: [] for column in styles_columns} 
            
            if self.album_artist != 'Various Artists':
                discogs_search = self.album_artist+' '+self.album_name            
            else:
                discogs_search = 'Various '+self.album_name
            results = self.d.search(discogs_search, type='release')
            release = results[0] 
            if results:
                for genre in release.genres:
                    genres_rows['id_album'].append(self.album_id)
                    genres_rows['genre_name'].append(genre) 
                for style in release.styles:
                    styles_rows['id_album'].append(self.album_id)
                    styles_rows['style_name'].append(style) 
            else:
                genres_rows['id_album'].append(self.album_id)
                genres_rows['genre_name'].append(None)
                styles_rows['id_album'].append(self.album_id)
                styles_rows['genre_name'].append(None) 
            self.genres_data = genres_rows
            self.styles_data = styles_rows
        except DiscogsException:
            self.all_success = False
        except Exception:
            self.all_success = False
   

    #Insert everything everywhere all at once
    def insert_album_data(self):
        start = time.time()
        self.fetch_albums_data()
        self.fetch_tracks()
        self.fetch_artists_data()
        self.fetch_track_ratings()
        self.fetch_album_ratings()
        self.fetch_genres_and_styles()

        if(self.all_success):      
            print(pd.DataFrame(self.albums_data))
            print(pd.DataFrame(self.tracks_data))
            print(pd.DataFrame(self.artists_data))
            print(pd.DataFrame(self.track_ratings_data)) 
            print(pd.DataFrame(self.album_ratings_data))
            print(pd.DataFrame(self.genres_data))
            print(pd.DataFrame(self.styles_data))
        else:
            print(type(self.albums_data))
            print(type(self.tracks_data))
            print(type(self.artists_data))
            print(type(self.track_ratings_data)) 
            print(type(self.album_ratings_data))
            print(type(self.genres_data))
            print(type(self.styles_data))
            print('Error obteniendo datos')   
        end = time.time()
        print('Tiempo tardado: ',end - start) 
        return
   

