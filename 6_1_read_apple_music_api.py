import app
import library.csv
import library.parser
import library.json
import library.file
import library.scan

import sys

track_database = app.settings["track_database"]
track_list_path = app.settings["apple_music"]["track_list"]
api_path = app.settings["apple_music"]["compressed"]


def create_track_list_profile():

    for data in library.json.import_json(api_path):

        if data["href"]:
            library.json.export_json(track_list_path+data["filename"]+".json",{
                "href":data["href"]
            })

def create_api_list():    
    array=[]
    for data in library.json.import_json(track_database):
        
        if library.file.file_does_not_exists(track_list_path+data["filename"]+".json"):
            array.append({
                    "filename":data["filename"],
                    "artist":data["artist"],
                    "track":data["track"],
                    "src":"https://music.apple.com/gb/search?term="+data["artist"]+" "+data["track"],
                    "href":""
                    
            })  
    library.json.export_json(api_path,array)


library.comment.returnMessage("Start")
create_track_list_profile()
create_api_list()
library.comment.returnMessage("Completed")

