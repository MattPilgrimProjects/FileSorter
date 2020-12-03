import app
import library.scan
import library.parser
import library.json
import library.file

import sys
track_database = app.settings["track_database"]
spotify_album_list_path = app.settings["spotify"]["album_list"]
amazon_affiliate_path = "Z:\\amazon\\processed\\"

def array_single(processed_path):

    profile = library.json.import_json(processed_path)
    
    href = str(profile["long_path"])

    return {
        "artist":profile["artist"],
        "album":profile["album"],
        "href":href.split('"')[1]
    }


for data in library.json.import_json(track_database):

    album_list_data = spotify_album_list_path+data["filename"]+".json"

    if library.file.file_exists(album_list_data):

        array=[]
        for schema in library.json.import_json(album_list_data):

            processed_path = amazon_affiliate_path+data["filename_artist"]+"-"+library.parser.change_to_url(schema["album"])+".json"

            if library.file.file_exists(processed_path):

                array.append(array_single(processed_path))
          
                library.json.export_json("Z:\\amazon\\sidebar\\"+data["filename"]+".json",array)
