import models
from sqlalchemy import text
from sqlalchemy.orm import Session
from get_bg_color import best_color

# as the album color was a late addition, this function was done to initialize all the colors of the albums..
# ...already in the database
# this was run only once

def init_all_color(): 
    with Session(models.engine) as session:
        session.begin()
        try:            
            albums_query = "select id, cover_url from albums where cover_color_to is null"
            albums = session.execute(text(albums_query) )
            for i, album in enumerate(albums):
                color_to = best_color(album[1])                           
                update_query = "update albums set cover_color_to = '{}' where id = '{}'".format(color_to, album[0])
                session.execute(text(update_query))

        except Exception as e:
            print(e)
            session.rollback()        
        else:
            print('commited')
            session.commit()

if __name__ == "__main__":
    init_all_color()
        