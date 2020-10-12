import schedule
import time

def job():
    print("Test return")

schedule.every(1).minutes.do(job)


while 1:
    schedule.run_pending()
    time.sleep(1)