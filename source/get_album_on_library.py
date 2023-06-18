import models
from sqlalchemy import text
from sqlalchemy.orm import Session


class AlbumInLibrary:
    def __init__(self,album_id):
        self.album_id = album_id

    
    def search_album(self):
        with Session(models.engine) as session:
            session.begin()
            try:
                query_album_exists = 'select id_album from album_ratings where id_album = :album_id and id_user = :user_id;'  
                album_in_lib =  session.execute(text(query_album_exists),{'album_id':self.album_id, 'user_id':1}).scalar()                                
                if not album_in_lib:
                    raise Exception('Album not in library')
                
                albumData = {
                    'release_type': None,
                    'album_name': None,
                    'artist_name': None,
                    'album_id': None,        
                    'rating': None,
                    'total_discs': None,
                    'total_tracks': None,
                    'release_date': None,
                    'cover_image': None,
                    'genres': [],
                    'styles': [],
                    'tracks': None
                }

                query_header = """select atypes.name release_type, a.name album_name, art.name artist_name, a.id album_id,
                arat.user_final_rating rating, t.total_discs, a.total_tracks, a.release_date, a.cover_url cover_image
                from albums a left join artists art on art.id = a.artist_id left join album_ratings arat on a.id = arat.id_album
                left join album_types atypes on a.type_id = atypes.id left join 
                (select max(disc_number) total_discs,album_id from tracks where album_id='{}') t
                on t.album_id = a.id where a.id='{}'""".format(self.album_id,self.album_id)
                    
                query_genres = "select genre_name from genres_by_album g where g.id_album='{}';".format(self.album_id)
                query_styles = "select style_name from styles_by_album s where s.id_album='{}';".format(self.album_id)

                query_tracks = """select t.id track_id, t.disc_number track_disc_number, t.track_number track_number_on_disc, t.name track_name,
                art.name track_artist, tr.rating track_ratings, tr.goated goated, tr.included, t.duration_ms track_duration_ms 
                from tracks t left join artists art on t.artist_id = art.id
                left join track_ratings tr on tr.id_track = t.id
                where t.album_id='{}' order by t.overall_number;""".format(self.album_id)

                album_header = session.execute(text(query_header))
                for row in album_header:            
                    albumData['release_type'] = row[0]
                    albumData['album_name'] = row[1]
                    albumData['artist_name'] = row[2]
                    albumData['album_id'] = row[3]
                    albumData['rating'] = 0 if row[4] == None else row[4]
                    albumData['total_discs'] = row[5]
                    albumData['total_tracks'] = row[6]
                    albumData['release_date'] = row[7]
                    albumData['cover_image'] = row[8] 

                album_genres = session.execute(text(query_genres))
                for row in album_genres:
                    albumData['genres'].append(row[0])  

                album_styles = session.execute(text(query_styles))
                for row in album_styles:
                    albumData['styles'].append(row[0])
                
                

                tracks_columns=['track_id', 'track_disc_number', 'track_number_on_disc', 'track_name','track_artist',
                'track_ratings', 'goated', 'included', 'track_duration_ms']
                discs = albumData['total_discs']
                albumData['tracks'] = [ [] for i in range(discs)]
                album_tracks = session.execute(text(query_tracks))
                for row in album_tracks:
                    disc = row[1] - 1
                    track_row = { column: None for column in tracks_columns }
                    track_row['track_id'] = row[0]
                    track_row['track_disc_number'] = row[1]
                    track_row['track_number_on_disc'] = row[2]
                    track_row['track_name'] = row[3]
                    track_row['track_artist'] = row[4]
                    track_row['track_ratings'] = 0 if row[5] == None else row[5]
                    track_row['goated'] = bool(row[6])
                    track_row['included'] = bool(row[7])
                    track_row['track_duration_ms'] = row[8]
                    albumData['tracks'][disc].append(track_row)
            except Exception as e:
                session.rollback()
                return False
            else:
               session.commit()
               return albumData
