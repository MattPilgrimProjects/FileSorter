import app
import library.scan
import library.parser
import library.json
import library.file

import sys
track_database = app.settings["track_database"]
spotify_album_list_path = app.settings["spotify"]["album_list"]
amazon_affiliate_path = "Z:\\amazon\\processed\\"

def href_single(schema):

    if library.file.file_exists(schema["process_path"]):
        return library.json.import_json(schema["process_path"])["href"]
    else:
        return schema["src"]



def sidebar_creator():
    for data in library.json.import_json("Z:\\amazon\\api.json"):

        array=[]

        for schema in library.json.import_json("Z:\\amazon\\api.json"):

            if data["song"] == schema["song"]:
                array.append({
                    "artist":schema["artist"],
                    "album":schema["album"],
                    "href":href_single(schema),
                    "album_artwork":schema["album_artwork"]
                })
        

        library.json.export_json("Z:\\amazon\\sidebar\\"+data["song"]+".json",array)

        library.comment.returnUpdateMessage("Processing: "+data["song"])

library.comment.returnMessage("Started")
sidebar_creator()
library.comment.returnMessage("Completed")