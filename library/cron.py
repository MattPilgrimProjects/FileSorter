import schedule
import time

def schedule_handler(seconds,functions):
    schedule.every(seconds).seconds.do(functions)

    while 1:
        schedule.run_pending()
        time.sleep(1)