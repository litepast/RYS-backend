import pandas as pd
import config
import datetime
from sqlalchemy import create_engine, text

class Album():

    user_id = 1
    album_name = None
    artist_name = None
    types_dict = {'album':1 , 'single':2, 'compilation':3 }
    all_artists = None
    tracks_ids = None
    no_tracks = None


    def __init__(self,album_id):
        self.album_id = album_id
        self.sp = config.sp
        self.d = config.d
       


    def get_albums(self):
        album = self.sp.album(self.album_id)    
        albums_columns = ['id', 'artist_id', 'type_id', 'name', 'release_date','release_precision', 'total_tracks', 'cover_url']        
        albums_rows = { column: [] for column in albums_columns}       
        albums_rows['id'].append(album['id'])
        albums_rows['artist_id'].append(album['artists'][0]['id'])
        albums_rows['type_id'].append(self.types_dict[album['album_type']])
        albums_rows['name'].append(album['name'])
        albums_rows['release_date'].append(album['release_date'])
        albums_rows['release_precision'].append(album['release_date_precision'])
        albums_rows['total_tracks'].append(album['total_tracks']) 
        albums_rows['cover_url'].append(album['images'][1]['url'])  
        self.album_name = album['name']
        self.artist_name = album['artists'][0]['name']
        self.no_tracks = album['total_tracks']
        return albums_rows


    def get_tracks(self):
        if self.no_tracks <= 50:         
            tracks_rows = self.get_tracks_onecall()
        else:
            limits=self.limit_per_tracks()
            tracks_rows = self.get_tracks_several(limits)
        return tracks_rows

    def get_tracks_onecall(self):
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
    
    
    def get_tracks_several(self,limits):
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
    

    def limit_per_tracks(self):
        n = self.no_tracks // 50
        mod = self.no_tracks % 50 
        limits = [50]*n
        if mod > 0:
            limits.append(mod)
        return limits

    def get_artists(self):
        artists_columns = [ 'id', 'name','popularity']
        artists_rows = { column: [] for column in artists_columns} 
        artists=self.slice_artists(self.all_artists)       
        for slice in artists:            
            artists_results=self.sp.artists(slice)
            artists_results=artists_results['artists']
            for artist in artists_results:
                artists_rows['id'].append(artist['id'])
                artists_rows['name'].append(artist['name'])
                artists_rows['popularity'].append(artist['popularity'])         
        return artists_rows 
           
    
    def slice_artists(self,all_artists):
       return [all_artists[index : index + 50] for index in range(0, len(all_artists), 50)]
    

    def get_album_ratings(self):
        aratings_columns = [ 'id_user', 'id_album','simple_avg_rating','more_than_nine_rating','weight_rating','suggested_rating_a','suggested_rating_b','user_final_rating','created_date','updated_date']
        aratings_rows = { column: [] for column in aratings_columns} 
        dt = datetime.datetime.now()              
        aratings_rows['id_user'].append(1) #cambiar usuario cuando se implemente login
        aratings_rows['id_album'].append(self.album_id)
        aratings_rows['simple_avg_rating'].append(0)
        aratings_rows['more_than_nine_rating'].append(0)
        aratings_rows['weight_rating'].append(1) 
        aratings_rows['suggested_rating_a'].append(0)
        aratings_rows['suggested_rating_b'].append(0)
        aratings_rows['user_final_rating'].append(0)
        aratings_rows['created_date'].append(dt) 
        aratings_rows['updated_date'].append(dt)          
        return aratings_rows
    

    def get_track_ratings(self):
        tratings_columns = [ 'id_user', 'id_track','rating','goated','included']
        tratings_rows = { column: [] for column in tratings_columns} 
        for track in self.tracks_ids:
            tratings_rows['id_user'].append(1) #cambiar usuario cuando se implemente login
            tratings_rows['id_track'].append(track)
            tratings_rows['rating'].append(0)
            tratings_rows['goated'].append(0)
            tratings_rows['included'].append(1)
        return tratings_rows

    def get_genres_and_styles(self):
        genres_columns = [ 'id_album', 'id_genre']
        genres_rows = { column: [] for column in genres_columns}
        styles_columns = [ 'id_album', 'id_style']
        styles_rows = { column: [] for column in styles_columns} 
        
        if self.artist_name != 'Various Artists':
            discogs_search = self.artist_name+' '+self.album_name            
        else:
            discogs_search = 'Various '+self.album_name
            
      
        results = self.d.search(discogs_search, type='release')
        release = results[0] 
        print(release.genres)
        print(release.styles)
        
        # if results:
        #     engine = create_engine(config.mysql_connection)
        #     with engine.connect() as connection:
        #         result = connection.execute(text("select name,id from genres union select name,id from styles"))        
        #         dict_genres = {row[0]:row[1] for row in result}
        #         release = results[0]            
        #         for genre in release.genres:
        #             genres_rows['id_album'].append(self.album_id)
        #             genres_rows['id_genre'].append(dict_genres[genre])                
        #         for style in release.styles:
        #             styles_rows['id_album'].append(self.album_id)
        #             styles_rows['id_style'].append(dict_genres[style])  

        # else:
        #             genres_rows['id_album'].append(self.album_id)
        #             genres_rows['id_genre'].append(None)                
        #             styles_rows['id_album'].append(self.album_id)
        #             styles_rows['style'].append(None)  
        return genres_rows,styles_rows

   

    #Insert everything
    def insert_album_data(self):
        albums_data = self.get_albums()
        tracks_data = self.get_tracks() 
        self.all_artists = list(set((albums_data['artist_id']+tracks_data['artist_id'])))
        self.tracks_ids = tracks_data['id']
        artists_data=self.get_artists()        
        tratings_data=self.get_track_ratings()
        aratings_data=self.get_album_ratings()
        gba_data, sba_data =self.get_genres_and_styles()
              
        tracks_df = pd.DataFrame(tracks_data)
        albums_df = pd.DataFrame(albums_data)
        artists_df=pd.DataFrame(artists_data)
        tratings_df=pd.DataFrame(tratings_data)  
        aratings_df=pd.DataFrame(aratings_data)
        gba_df=pd.DataFrame(gba_data)
        sba_df=pd.DataFrame(sba_data)

        print(albums_df)
        print(artists_df)
        print(tracks_df)
        print(tratings_df)
        print(aratings_df)
        print(gba_df)
        print(sba_df)
        return
   

