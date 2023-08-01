import models
from sqlalchemy import text
from sqlalchemy.orm import Session


class Library:
    def __init__(self,query):
        self.query = query
    
    def construct_query_text(self):
        select = """select a.id album_id, art.name artist_name, a.name,  left(a.release_date,4) as release_year, a.cover_url, ar.user_final_rating
        from albums a left join album_ratings ar on a.id = ar.id_album left join artists art on art.id = a.artist_id """

        query_rating_null = ''
        query_ratings = ''
        query_years = ''
        query_types = ''
        query_artist = ''
        query_album = ''
        query_genres = ''
        query_styles = ''

        list_where = []
        list_where_ratings = []
        list_where_else = []
        list_where_styles = []


        if 'ratings[]' in self.query:
            if 'Unrated' in self.query['ratings[]']:
                query_rating_null =  'ar.user_final_rating is null'        
                self.query['ratings[]'] = [float(x) for x in self.query['ratings[]'] if x != 'Unrated']
                list_where_ratings.append(query_rating_null)
            if len(self.query['ratings[]']) > 0:
                query_ratings = 'ar.user_final_rating in (' + ','.join([str(x) for x in self.query['ratings[]']]) + ')'
                list_where_ratings.append(query_ratings)  

        if 'years[]' in self.query:    
            self.query['years[]'] = [int(x) for x in self.query['years[]']]
            query_years = 'left(a.release_date,4) in (' + ','.join([str(x) for x in self.query['years[]']]) + ')'
            list_where_else.append(query_years)    

        if 'types[]' in self.query:    
            self.query['types[]'] = [int(x) for x in self.query['types[]']]
            query_types = 'a.type_id in (' + ','.join([str(x) for x in self.query['types[]']]) + ')'
            list_where_else.append(query_types)

        if self.query['artist_name'][0] != '':
            query_artist = 'art.name like "%' + self.query['artist_name'][0] + '%"'
            list_where_else.append(query_artist)

        if self.query['album_name'][0] != '':
            query_album = 'a.name like "%' + self.query['album_name'][0] + '%"'
            list_where_else.append(query_album)

        if 'genres[]' in self.query:
            if 'Without Genre' in self.query['genres[]']:
                self.query['genres[]'] = ['NOT_FOUND' if x == 'Without Genre' else x for x in self.query['genres[]']]
            query_genres = 'select distinct(id_album) from genres_by_album where genre_name in ("' + '","'.join(self.query['genres[]']) + '")'
            
        if 'styles[]' in self.query:
            if 'Without Style' in self.query['styles[]']:
                self.query['styles[]'] = ['NOT_FOUND' if x == 'Without Style' else x for x in self.query['styles[]']]
            query_styles = 'select distinct(id_album) from styles_by_album where style_name in ("' + '","'.join(self.query['styles[]']) + '")'

        if query_genres and query_styles:
            list_where_styles.append( 'a.id in ( select distinct(id_album) from ( ' + query_genres + ' union ' + query_styles + ' ) x )' )
        elif query_genres:
            list_where_styles.append( 'a.id in ( ' + query_genres + ' )' )
        elif query_styles:
            list_where_styles.append( 'a.id in ( ' + query_styles + ' )' )

        if list_where_ratings:
            if len(list_where_ratings) > 1:
                where1 = '('+' or '.join(list_where_ratings)+')'
            else:
                where1 = list_where_ratings[0]
            list_where.append(where1)

        if list_where_else:
            where2 = ' and '.join(list_where_else)
            list_where.append(where2)

        if list_where_styles:
            list_where.append(list_where_styles[0])  

        if list_where:
            select = select + ' where ' + ' and '.join(list_where) + ' order by 2, 3'
        else:
            select = select + ' limit 2500'
                    
        return(select)


    def search_album(self):
        with Session(models.engine) as session:
            session.begin()
            try:
                results_columns = ['name', 'artist', 'album_id', 'release_date', 'cover_url', 'rating']   
                results_object = []
                query_text = self.construct_query_text()
                genres_data = session.execute(text(query_text))
                for row in genres_data:
                    results_rows = { column: None for column in results_columns}
                    results_rows['album_id'] = row[0]                    
                    results_rows['artist'] = row[1]
                    results_rows['name']= row[2]
                    results_rows['release_date'] = row[3]
                    results_rows['cover_url'] = row[4]
                    results_rows['rating'] = row[5]
                    results_object.append(results_rows)
            except Exception as e:
                session.rollback()
                return(False)        
            else:
                session.commit()
                return(results_object)
            
        
       