import pandas as pd
import datetime
import time
import models
from spotipy import SpotifyException
from discogs_client.exceptions import HTTPError as DiscogsException
from sqlalchemy import text
from sqlalchemy.orm import Session
from get_bg_color import best_color
import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
import config

# given the spotify id of an album, it will insert all of its relevant data to our app on the rys db..
# this is used on the '+' button on each album cover after a serach has been made on...
# on the '/' or '/search' url on the webapp
# if the album already exists, it will not insert anything 


class Album():
   
    def __init__(self,album_id):
        self.user_id = 1 
        self.album_id = album_id        
        self.all_success = True
        self.sp = config.sp
        self.d = config.d

    # gets the album data (doesn't include songs or artists) from spotify api via spotipy library, this is the main method used on..
    # ...all functions on this file
    def fetch_albums_data(self):
        try: 
            types_dict = {'album':1 , 'single':2, 'compilation':3 }
            album_data = []
            album = self.sp.album(self.album_id)    
            albums_columns = ['id', 'artist_id', 'type_id', 'name', 'release_date','release_precision', 'total_tracks', 'cover_url', 'cover_color']        
            albums_rows = { column : None  for column in albums_columns}       
            albums_rows['id'] = album['id']
            albums_rows['artist_id'] = album['artists'][0]['id']
            albums_rows['type_id'] = types_dict[album['album_type']]
            albums_rows['name'] = album['name']
            albums_rows['release_date'] = album['release_date']
            albums_rows['release_precision'] = album['release_date_precision']
            albums_rows['total_tracks'] = album['total_tracks']
            albums_rows['cover_url']=album['images'][1]['url'] 
            albums_rows['cover_color'] = best_color(albums_rows['cover_url'])
            self.no_tracks =  albums_rows['total_tracks']            
            self.album_artist = album['artists'][0]['name']            
            self.album_name = album['name']  
            album_data.append(albums_rows)          
            self.albums_data = album_data
        except SpotifyException:
            self.all_success = False
        except Exception:
            self.all_success = False

    #gets all the spotify data from the album
    def fetch_tracks(self): 
        # the spotify app only allows getting data from 50 songs at most in one request...
        # so in case an album has more than 50 songs, there needs to be more than one request

        # this function runs in case the album has less than 50 songs
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

        #this funtion runs in case the album has more than 50 songs                 
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

        #this funtions check if we can do it on one request or there needs to be several requests        
        def limits_per_call():
            n = self.no_tracks // 50
            mod = self.no_tracks % 50 
            limits = [50]*n
            if mod > 0:
                limits.append(mod)
            return limits

        #finally the code the saves the request on the class data            
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

    # same case as with the songs, spotofy doesn't allow to fetch more than 50 artists in one request on its api...
    # in the case of 'Various Artists' album, there might be more than 50 artists on it
    # as we save some data of each artist of each album track

    def fetch_artists_data(self):

        # here I tried a different approach
        # first i save all the aritsts spotify ids in a list, regards is only 1 artists or more thn 50
        # those are got from the tracks request
        def combine_artists():
            if (self.albums_data and self.tracks_data):
                artist_tracks = [row['artist_id'] for row in self.tracks_data]
                artist_album = [self.albums_data[0]['artist_id']]
                self.all_artists = list(set((artist_album + artist_tracks )))
                return True
            else:
                return False

        #the list from above is sliced in several sub lists, sized 50
        def slice_artists(all_artists):
            return [all_artists[index : index + 50] for index in range(0, len(all_artists), 50)]

        #finally given the number of slices, it will be adding the aritsts data from the spotofy api via spotipy
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

    #it initializes the album several ratings as none (null in mysql)
    def fetch_album_ratings(self):
        try:
            album_ratings_data = []
            aratings_columns = ['id_user', 'id_album',                               
                                'simple_average_rating','weighted_average_rating','consistency_rating','greatness_rating',    
                                'suggested_rating_a','suggested_rating_b','suggested_rating_final','user_final_rating',
                                'created_date','updated_date']
            aratings_rows = { column: None for column in aratings_columns} 
            dt = datetime.datetime.now()              
            aratings_rows['id_user'] = self.user_id 
            aratings_rows['id_album'] = self.album_id
            aratings_rows['created_date'] = dt 
            aratings_rows['updated_date'] = dt
            album_ratings_data.append(aratings_rows)  
            self.album_ratings_data = album_ratings_data
        except Exception:
            self.all_success = False 
    
    #it initializes the track ratings of the new album
    def fetch_track_ratings(self):
        try:
            track_ratings_data = []
            tratings_columns = [ 'id_user', 'id_track','rating','goated','included']
            for track in self.id_tracks:
                tratings_rows = { column: None for column in tratings_columns} 
                tratings_rows['id_user'] = self.user_id 
                tratings_rows['id_track'] = track
                tratings_rows['goated'] = 0
                tratings_rows['included'] = 1
                track_ratings_data.append(tratings_rows)
            self.track_ratings_data =  track_ratings_data
        except Exception:
            self.all_success = False 
            

    # as spotify does poorly with the genres of an album, in order to get the genre of the album..
    # we connect to the Discogs (discogs.com) Api, the most complete music database online
    # we use its api via the library discogs_client
    # we sent the album name and artists and get two lists, one for genres and another for styles

    def fetch_genres_and_styles(self):
        try:
            genres_columns = ['id_album', 'genre_name']            
            styles_columns = ['id_album', 'style_name']
            genres_data = []
            styles_data = []
            if self.album_artist != 'Various Artists':
                discogs_search = self.album_name+' '+self.album_artist           
            else:
                discogs_search = 'Various '+self.album_name
            print('trying: ',discogs_search)
            results = self.d.search(discogs_search, type='release')             
            release = None       

            #checks it the search brings results and that results has genres and styles assigned
            if results: 
                for result in results:
                    if (result.genres and result.styles):
                        release = result
                        break
            # if the first match has genres and styles, it will save them to the class data, otherwise it will...
            # ...assign them as none (NOT_FOUND per mysql rys db rules)
            if release:
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
                styles_rows['id_album'] = self.album_id
                genres_data.append(genres_rows)
                styles_data.append(styles_rows) 
            self.genres_data = genres_data
            self.styles_data = styles_data
        except DiscogsException:
            print('discogs exp: ', e)
            
            self.all_success = False
        except Exception as e:
            print('Py exp: ', e)
            self.all_success = False
   

    # runs all functions to get the data ready to insert, it will return true only if all
    # functions ran succesfully    
    def fetch_all_data(self):
        functions = [self.fetch_albums_data, self.fetch_tracks, self.fetch_artists_data, 
                     self.fetch_genres_and_styles, self.fetch_track_ratings,self.fetch_album_ratings]        
        for fun in functions:
            fun()
            if not self.all_success:
                print('funcion fallida: ',fun, self.album_id)
                return False       
        return self.all_success


    #finally, if all fetchin functions ran without issue, it inserts all the data to the rys db
    def insert_album_data(self):
        start = time.time()
        with Session(models.engine) as session:
            session.begin()
            try:
                q1 = 'select id_album from album_ratings where id_album = :album_id and id_user = :user_id;'
                q2 = 'select id from albums where id = :album_id'
                album_in_user = session.execute(text(q1),{'album_id':self.album_id, 'user_id':self.user_id}).scalar()                
                album_in_sys = session.execute(text(q2), {'album_id':self.album_id}).scalar()                                
                #if album already exists..
                if album_in_user:
                    msg = 'Album already in Library'
                elif album_in_sys:
                    #si el album esta en sistema pero no esta en la del ususario
                    q3='insert into track_ratings (select :user_id, id, null, 0, 1 from tracks where album_id= :album_id);'
                    q4='insert into album_ratings values (:user_id, :album_id,null,null,null,null,null,null,now(),now());'
                    session.execute(text(q3),{'album_id':self.album_id, 'user_id':self.user_id})
                    session.execute(text(q4),{'album_id':self.album_id, 'user_id':self.user_id})               
                    msg = 'New album added to Library!' 
                ##here it inserts all the data finally!              
                elif self.fetch_all_data():
                    for row in self.artists_data:
                        record = models.rys_artist(**row)
                        session.merge(record)            
                    record = models.rys_albums(**self.albums_data[0])
                    session.add(record)            
                    for row in self.tracks_data:
                        record = models.rys_tracks(**row)
                        session.add(record)            
                    for row in self.genres_data:
                        record = models.rys_genres(**row)
                        session.add(record)
                    for row in self.styles_data:
                        record = models.rys_styles(**row)
                        session.add(record)            
                    record = models.rys_album_ratings(**self.album_ratings_data[0])
                    session.add(record)
                    for row in self.track_ratings_data:
                        record = models.rys_tracks_ratings(**row)
                        session.add(record)                
                    msg = 'New album added to Library!'
                else:
                    raise Exception("Error connecting to Spotify!")
            except Exception as e:
                session.rollback()
                msg = e
                end = time.time()
                print('tiempo de todo ', end - start)
                return False,msg
            else:
                session.commit()
                end = time.time()
                print('tiempo de todo ', end - start)
                print('checalo')
                return True,msg
       
        
            
            
   

