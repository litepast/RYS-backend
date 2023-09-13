import models
from sqlalchemy import text
from sqlalchemy.orm import Session

class DeleteAlbum:
    def __init__(self, album_id):
        self.album_id = album_id

    def delete_album(self):
        with Session(models.engine) as session:
            session.begin()
            try:  
                print(self.album_id)              
                delete_tr = "delete from track_ratings where id_track in (select id from tracks where album_id  = '{}')".format(self.album_id)
                delete_tx = "delete from tracks where album_id  = '{}'".format(self.album_id)
                delete_ar = "delete from album_ratings where id_album = '{}'".format(self.album_id)
                delete_gn = "delete from genres_by_album where id_album = '{}'".format(self.album_id)
                delete_st = "delete from styles_by_album where id_album = '{}'".format(self.album_id)
                delete_ab = "delete from albums where id = '{}'".format(self.album_id)

                delete_art="""delete from artists where
                            not exists (select * from tracks where artists.id = tracks.artist_id)
                            and artists.id <> '0LyfQWJT6nXafLPZqxe9Of'
                            and artists.id <> '6NeoLSPGwJLfeisvM36SMi'                            
                            """
                
                
                session.execute(text(delete_tr))
                session.execute(text(delete_tx))
                session.execute(text(delete_ar))
                session.execute(text(delete_gn))
                session.execute(text(delete_st))
                session.execute(text(delete_ab))
                session.execute(text(delete_art)) 
                                  

            except Exception as e:
                print(e)
                session.rollback()
                return False        
            else:                
                session.commit()
                print("Album deleted")
                return True
