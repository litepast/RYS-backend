import pandas as pd
import config
import datetime
import time
from spotipy import SpotifyException
from discogs_client.exceptions import HTTPError as DiscogsException
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.automap import automap_base

class Album():
   
    def __init__(self,album_id):
        self.user_id = 1 
        self.album_id = album_id        
        self.all_success = True
        self.sp = config.sp
        self.d = config.d


    def fetch_albums_data(self):
        try: 
            types_dict = {'album':1 , 'single':2, 'compilation':3 }
            album_data = []
            album = self.sp.album(self.album_id)    
            albums_columns = ['id', 'artist_id', 'type_id', 'name', 'release_date','release_precision', 'total_tracks', 'cover_url']        
            albums_rows = { column : None  for column in albums_columns}       
            albums_rows['id'] = album['id']
            albums_rows['artist_id'] = album['artists'][0]['id']
            albums_rows['type_id'] = types_dict[album['album_type']]
            albums_rows['name'] = album['name']
            albums_rows['release_date'] = album['release_date']
            albums_rows['release_precision'] = album['release_date_precision']
            albums_rows['total_tracks'] = album['total_tracks']
            albums_rows['cover_url']=album['images'][1]['url'] 
            self.no_tracks =  albums_rows['total_tracks']            
            self.album_artist = album['artists'][0]['name']            
            self.album_name = album['name']  
            album_data.append(albums_rows)          
            self.albums_data = album_data
        except SpotifyException:
            self.all_success = False
        except Exception:
            self.all_success = False


    def fetch_tracks(self): 
        def fetch_tracks_onecall():
            tracks_result = self.sp.album_tracks(self.album_id)        
            tracks_result = tracks_result['items']
            tracks_data = []
            tracks_columns = ['id', 'album_id', 'artist_id', 'disc_number','track_number','overall_number','name','duration_ms']            
            for i,track in enumerate(tracks_result, 1): 
                tracks_rows = {column: None for column in tracks_columns} 
                tracks_rows['id'] = track['id']
                tracks_rows['album_id'] = self.album_id
                tracks_rows['artist_id']= track['artists'][0]['id']
                tracks_rows['disc_number'] = track['disc_number']
                tracks_rows['track_number'] = track['track_number']
                tracks_rows['overall_number'] = i 
                tracks_rows['name'] = track['name']
                tracks_rows['duration_ms'] = track['duration_ms']                
                tracks_data.append(tracks_rows)           
            return tracks_data                 
        def fetch_tracks_several(limits):
            tracks_columns = [ 'id', 'album_id', 'artist_id', 'disc_number','track_number','overall_number','name','duration_ms']
            tracks_data = []
            for n,limit in enumerate(limits):          
                tracks_result = self.sp.album_tracks(self.album_id,limit=limit,offset=(n*50))
                tracks_result = tracks_result['items']
                for i,track in enumerate(tracks_result, 1):
                    tracks_rows = { column: None for column in tracks_columns}  
                    tracks_rows['id'] = track['id']
                    tracks_rows['album_id'] = self.album_id
                    tracks_rows['artist_id']= track['artists'][0]['id']
                    tracks_rows['disc_number'] = track['disc_number']
                    tracks_rows['track_number'] = track['track_number']
                    tracks_rows['overall_number'] = (n*50)+i
                    tracks_rows['name'] = track['name']
                    tracks_rows['duration_ms'] = track['duration_ms']                    
                    tracks_data.append(tracks_rows) 
            return tracks_data        
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
            else:            
                self.tracks_data = fetch_tracks_several(limits_per_call())              
            self.id_tracks = [row['id'] for row in self.tracks_data]              
        except SpotifyException:
            self.all_success = False
        except IndexError:
            self.all_success = False
        except Exception:
            self.all_success = False


    def fetch_artists_data(self):
        def combine_artists():
            if (self.albums_data and self.tracks_data):
                artist_tracks = [row['artist_id'] for row in self.tracks_data]
                artist_album = [self.albums_data[0]['artist_id']]
                self.all_artists = list(set((artist_album + artist_tracks )))
                return True
            else:
                return False
        def slice_artists(all_artists):
            return [all_artists[index : index + 50] for index in range(0, len(all_artists), 50)]
        try:
            if(combine_artists()):
                artists_columns = ['id', 'name','popularity']
                artists_data = []
                artists=slice_artists(self.all_artists)    
                for slice in artists:            
                    artists_results=self.sp.artists(slice)
                    artists_results=artists_results['artists']
                    for artist in artists_results:
                        artists_rows = { column: None for column in artists_columns} 
                        artists_rows['id'] = artist['id']
                        artists_rows['name'] = artist['name']
                        artists_rows['popularity'] = artist['popularity']
                        artists_data.append(artists_rows)
                self.artists_data = artists_data 
            else: 
                self.all_success = False 
        except SpotifyException:
            self.all_success = False 
        except Exception:
            self.all_success = False   


    def fetch_album_ratings(self):
        try:
            album_ratings_data = []
            aratings_columns = [ 'id_user', 'id_album','simple_avg_rating','more_than_nine_rating','weight_rating','suggested_rating_a','suggested_rating_b','user_final_rating','created_date','updated_date']
            aratings_rows = { column: None for column in aratings_columns} 
            dt = datetime.datetime.now()              
            aratings_rows['id_user'] = 1 #cambiar usuario cuando se implemente login
            aratings_rows['id_album'] = self.album_id
            ##aratings_rows['simple_avg_rating'].append(None)
            ##aratings_rows['more_than_nine_rating'].append(None)
            ##aratings_rows['weight_rating'].append(1) 
            ##aratings_rows['suggested_rating_a'].append(None)
            ##aratings_rows['suggested_rating_b'].append(None)
            ##aratings_rows['user_final_rating'].append(None)
            aratings_rows['created_date'] = dt 
            aratings_rows['updated_date'] = dt
            album_ratings_data.append(aratings_rows)  
            self.album_ratings_data = album_ratings_data
        except Exception:
            self.all_success = False 
    

    def fetch_track_ratings(self):
        try:
            track_ratings_data = []
            tratings_columns = [ 'id_user', 'id_track','rating','goated','included']
            for track in self.id_tracks:
                tratings_rows = { column: None for column in tratings_columns} 
                tratings_rows['id_user'] = 1 #cambiar usuario cuando se implemente login
                tratings_rows['id_track'] = track
                #tratings_rows['rating'].append(None)
                tratings_rows['goated'] = 0
                tratings_rows['included'] = 1
                track_ratings_data.append(tratings_rows)
            self.track_ratings_data =  track_ratings_data
        except Exception:
            self.all_success = False 


    def fetch_genres_and_styles(self):
        try:
            genres_columns = [ 'id_album', 'genre_name']            
            styles_columns = [ 'id_album', 'style_name']
            genres_data = []
            styles_data = []
            if self.album_artist != 'Various Artists':
                discogs_search = self.album_artist+' '+self.album_name            
            else:
                discogs_search = 'Various '+self.album_name
            results = self.d.search(discogs_search, type='release')
            release = results[0] 
            if results:
                for genre in release.genres:
                    genres_rows = { column: None for column in genres_columns}
                    genres_rows['id_album'] = self.album_id
                    genres_rows['genre_name'] = genre 
                    genres_data.append(genres_rows)
                for style in release.styles:
                    styles_rows = { column: None for column in styles_columns} 
                    styles_rows['id_album'] = self.album_id
                    styles_rows['style_name'] = style 
                    styles_data.append(styles_rows)
            else:
                genres_rows = { column: None for column in genres_columns}
                styles_rows = { column: None for column in styles_columns} 
                genres_rows['id_album'] = self.album_id
                #genres_rows['genre_name'].append(None)
                styles_rows['id_album'] = self.album_id
                #styles_rows['genre_name'].append(None)
                genres_data.append(genres_rows)
                styles_data.append(styles_rows) 
            self.genres_data = genres_data
            self.styles_data = styles_data
        except DiscogsException:
            self.all_success = False
        except Exception:
            self.all_success = False
   

    #Fetch All data to Insert
    def fetch_album_data(self):
        self.fetch_albums_data()
        self.fetch_tracks()
        self.fetch_artists_data()
        self.fetch_genres_and_styles()
        return self.all_success
    
    def create_user_ratings(self):
        self.fetch_track_ratings()
        self.fetch_album_ratings()
        return
    
    def print_inserted_data(self):
        if(self.all_success):    
            print(pd.DataFrame(self.albums_data),end='\n\n')
            print(pd.DataFrame.from_dict(self.tracks_data),end='\n\n')
            print(pd.DataFrame(self.artists_data),end='\n\n')
            print(pd.DataFrame(self.track_ratings_data),end='\n\n')
            print(pd.DataFrame(self.album_ratings_data),end='\n\n')
            print(pd.DataFrame(self.genres_data),end='\n\n')
            print(pd.DataFrame(self.styles_data),end='\n\n')
        return


    def insert_album_data(self):
        self.fetch_album_data()
        self.create_user_ratings()       
        #self.print_inserted_data()
        engine = create_engine(config.mysql_connection)
        Base = automap_base()
        Base.prepare(autoload_with=engine)
        rys_artist = Base.classes.artists
        rys_albums = Base.classes.albums
        rys_tracks = Base.classes.tracks
        rys_genres = Base.classes.genres_by_album
        # rys_styles = Base.classes.styles_by_album
        # rys_album_ratings = Base.classes.album_ratings
        # rys_tracks_ratings = Base.classes.track_ratings
        

        with Session(engine) as session,session.begin():
            for row in self.artists_data:
                record = rys_artist(**row)
                session.add(record)
            
            record = rys_albums(**self.albums_data[0])
            session.add(record)
            
            for row in self.tracks_data:
                record = rys_tracks(**row)
                session.add(record)
            
            # for row in self.album_ratings_data:
            #     record = rys_album_ratings(**row)
            #     session.add(record)

            # for row in self.track_ratings_data:
            #     record = rys_tracks_ratings(**row)
            #     session.add(record)

            for row in self.genres_data:
                record = rys_genres(**row)
                session.add(record)

            # for row in self.styles_data:
            #     record = rys_styles(**row)
            #     session.add(record)

            #record = rys_albums(**self.albums_data)
            #session.add(record)
            #session.commit()
            print('checalo')  
               
  
    #    if album_id en albums_ratgins con usuario 1 
    #         # no inserta nada, album ya existe en libreria del usuario
    #         regresa            
    #     if album not en album headers
    #         #datos del album ya estan en base pero no los tiene el susuario
    #         joins para inicializar los user ratings con sql
    #         regresa            
    #     #si llegara ha esta punto, el album no esta para nada, hacer todo
    #         insera usuario data
    #         inserta todo
    #         regresa
        return 
   

