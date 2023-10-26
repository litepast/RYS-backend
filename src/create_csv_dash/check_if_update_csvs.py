import datetime
from config import engine
from sqlalchemy import text
from sqlalchemy.orm import Session


def check_if_update_csvs():
    with Session(engine) as session:
        session.begin()
        try:
            minutes_check = 10
            last_update_q= """select max(date) from ((select created_date as date from album_ratings order by 1 desc limit 1)
            union (select updated_date as date from album_ratings order by 1 desc limit 1)) A"""
        
            last_updated_date = session.execute(text(last_update_q)).fetchall()[0][0]
            current_date = datetime.datetime.now()

            difference_delta = current_date - last_updated_date
            difference_minutes = difference_delta.total_seconds() / 60

            if(difference_minutes < minutes_check ):
                update_csvs = True
            else:
                with open("./create_csv_dash/etl_date.txt", "r") as f:
                    etl_date = f.read()
                    etl_date = datetime.datetime.strptime(etl_date, '%Y-%m-%d %H:%M:%S.%f')
                    diff = current_date - etl_date
                    diff_minutes = diff.total_seconds() / 60
                    if(diff_minutes > minutes_check ):
                        update_csvs = True
                    else:
                         update_csvs = False
            
            #save current date to etl_date.txt
            with open("./create_csv_dash/etl_date.txt", "w") as f:
                f.write(str(current_date))
            

        except Exception as e:
            print(e)        
            session.rollback()             
            return False                    
        else:            
            return update_csvs







