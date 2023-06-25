import models
from sqlalchemy import text
from sqlalchemy.orm import Session

class UpdateRatings:
    def __init__(self, data_ratings):
        self.data_ratings = data_ratings

    def update_ratings(self):
        # print(self.data_ratings['data']['ar'])
        # print(self.data_ratings['data']['tr'])

        with Session(models.engine) as session:
            session.begin()
            try:
                sav = 'null' if self.data_ratings['data']['ar']['simple_average_rating'] == 0 else self.data_ratings['data']['ar']['simple_average_rating']
                war = 'null' if self.data_ratings['data']['ar']['weighted_average_rating'] == 0 else self.data_ratings['data']['ar']['weighted_average_rating']
                cr = 'null' if self.data_ratings['data']['ar']['consistency_rating'] == 0 else self.data_ratings['data']['ar']['consistency_rating']
                gr = 'null' if self.data_ratings['data']['ar']['greatness_rating'] == 0 else self.data_ratings['data']['ar']['greatness_rating']
                sra = 'null' if self.data_ratings['data']['ar']['suggested_rating_a'] == 0 else self.data_ratings['data']['ar']['suggested_rating_a']
                srb = 'null' if self.data_ratings['data']['ar']['suggested_rating_b'] == 0 else self.data_ratings['data']['ar']['suggested_rating_b']
                srf = 'null' if self.data_ratings['data']['ar']['suggested_rating_final'] == 0 else self.data_ratings['data']['ar']['suggested_rating_final']
                ufr = 'null' if self.data_ratings['data']['ar']['user_final_rating'] == 0 or self.data_ratings['data']['ar']['user_final_rating'] is None else self.data_ratings['data']['ar']['user_final_rating']
                ud = self.data_ratings['data']['ar']['updated_date']
                ai = self.data_ratings['data']['ar']['album_id']

             
                album_ratings_query = """                
                update album_ratings set
                simple_average_rating = {},
                weighted_average_rating = {},
                consistency_rating = {},
                greatness_rating = {},     
                suggested_rating_a = {},
                suggested_rating_b = {},
                suggested_rating_final = {},
                user_final_rating = {},
                updated_date = '{}'
                where id_album = '{}' and id_user = 1
                """.format(sav,war, cr, gr, sra, srb, srf, ufr, ud, ai )
                
                session.execute(text(album_ratings_query))

                for track in self.data_ratings['data']['tr']:
                    
                    
                    tr = 'null' if track['track_rating'] == 0 else track['track_rating']
                    trg = int(track['goated'])
                    tri = int(track['included'])
                    trid = track['track_id']
                    trq = "update track_ratings set rating = {}, goated = {}, included = {} where id_track = '{}' and id_user = 1".format(tr, trg, tri, trid )
                    session.execute(text(trq))
                               
                
                
                

            except Exception as e:
                print(e)
                session.rollback()
                return False        
            else:                
                session.commit()
                print("Ratings updated")
                return True
