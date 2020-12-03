import app
import library.scan
import library.parser
import library.file
import library.json
import library.csv
import library.directory

import sys

track_database = app.settings["track_database"]

album_list_path =app.settings["spotify"]["album_list"]

def update_api_list():
    raw=[]
    for data in library.json.import_json(track_database):

        album_list = album_list_path+data["filename"]+".json"

        if library.file.file_exists(album_list):
            array=[]
            for schema in library.json.import_json(album_list):

                raw_data_path = "Z:\\amazon\\processed\\"+data["filename_artist"]+"-"+library.parser.change_to_url(schema["album"])+".json"
                
                if library.file.file_does_not_exists(raw_data_path):

                    raw.append({
                                    "artist": data["artist"],
                                    "album":schema["album"],
                                    "src": "https://www.amazon.co.uk/s?k="+data["artist"]+" "+schema["album"]+"&i=popular&ref=nb_sb_noss",
                                    "short_path":"",
                                    "long_path":"",
                                    "album_artwork":schema["album_artwork"],
                                    "process_path":raw_data_path
                    })
        
            
    library.json.export_json("Z:\\amazon\\api.json",raw)

def add_to_processed_list():

    for data in library.json.import_json("Z:\\amazon\\api.json"):

        if data["long_path"]:
            library.json.export_json(data["process_path"],data)


            
add_to_processed_list()
update_api_list()


