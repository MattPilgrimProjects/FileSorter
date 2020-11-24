from datetime import datetime

def get_current_date():
    now = datetime.now()
    return now.strftime("%H:%M:%S")

def returnMessage(text):
    return print(get_current_date() +" => "+ text+"                                                    ")

def returnUpdateMessage(text):
    return print(get_current_date() +" => "+ text+"                                                    ",end="\r")