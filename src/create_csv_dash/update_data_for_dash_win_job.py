import threading
import time
from check_if_update_csvs import check_if_update_csvs
from update_csvs import update_csvs
import schedule
import datetime

##the idea is to launch this thread that will check if there has been an update in the rys db..
#then update the csvs used by the dash dashboard


minutes = 10

def task():
    if check_if_update_csvs():
        update_csvs()
        print(datetime.datetime.now(), " - Updated the csvs for dash to display")
    else:
        print(datetime.datetime.now(), " - No update in the db in the last 10 minutes")

def scheduled_task():
    schedule.every(minutes).minutes.do(task)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    threading.Thread(target=scheduled_task).start()
   
  
