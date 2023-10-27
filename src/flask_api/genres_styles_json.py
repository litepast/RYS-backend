import models
import json
from sqlalchemy import text
from sqlalchemy.orm import Session


def genres_to_jason(): 
    with Session(models.engine) as session:
        session.begin()
        try:
            genres_columns = ['id', 'name', 'selected','hover'] 
            genres_object = []
            genres_query = 'select id, name from genres'
            genres_data = session.execute(text(genres_query))
            for row in genres_data:
                genres_rows = { column: None for column in genres_columns}
                genres_rows['id'] = row[0]
                genres_rows['name'] = row[1]
                genres_rows['selected'] = False
                genres_rows['hover'] = False
                genres_object.append(genres_rows)

            styles_columns = ['id', 'name', 'selected','hover'] 
            styles_object = []
            styles_query = 'select id, name from styles'
            styles_data = session.execute(text(styles_query))
            for row in styles_data:
                styles_rows = { column: None for column in styles_columns}
                styles_rows['id'] = row[0]
                styles_rows['name'] = row[1]
                styles_rows['selected'] = False
                styles_rows['hover'] = False
                styles_object.append(styles_rows)
            

            with open("./data/genres_jsons/genres.json", "w") as outfile:
                 json.dump(genres_object, outfile)

            with open("./data/genres_jsons/styles.json", "w") as outfile:
                 json.dump(styles_object, outfile)

        except Exception as e:
            session.rollback()        
        else:
            session.commit()


if __name__ == "__main__":
       genres_to_jason()
        