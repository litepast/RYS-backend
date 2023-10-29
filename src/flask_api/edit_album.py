import models
from sqlalchemy import text
from sqlalchemy.orm import Session

#it will update the type, genres and style of one album
#used on the '/library/<album id>' url on the web app, on the pen button on the album cover
class EditAlbum():
    def __init__(self,params):
        self.params = params['params']
  
    def edit_album(self):
        with Session(models.engine) as session:
            session.begin()
            try:

                delete_genres = "delete from genres_by_album where id_album = '{}'".format(self.params['id'])
                delete_styles = "delete from styles_by_album where id_album = '{}'".format(self.params['id'])
                update_type = "update albums set type_id = '{}' where id = '{}'".format(self.params['release_type'],self.params['id'])

                session.execute(text(delete_genres))
                session.execute(text(delete_styles))
                session.execute(text(update_type))

                if self.params['genres']:
                    for genre in self.params['genres']:
                        insert_genres = "insert into genres_by_album (id_album, genre_name) values ('{}','{}')".format(self.params['id'],genre)
                        session.execute(text(insert_genres))
                else:
                    insert_genres = "insert into genres_by_album (id_album, genre_name) values ('{}','{}')".format(self.params['id'],'NOT_FOUND')
                    session.execute(text(insert_genres))

                if self.params['styles']:
                    for style in self.params['styles']:
                        insert_styles = "insert into styles_by_album (id_album, style_name) values ('{}','{}')".format(self.params['id'],style)
                        session.execute(text(insert_styles))
                else:
                    insert_styles = "insert into styles_by_album (id_album, style_name) values ('{}','{}')".format(self.params['id'],'NOT_FOUND')
                    session.execute(text(insert_styles))

            except Exception as e:
                print(e)
                session.rollback()
                return False        
            else:
                print("Album edited")
                session.commit()
                return True
            
        
       