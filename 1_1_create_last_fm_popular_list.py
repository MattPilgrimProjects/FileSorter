import app
import library.json
import library.scan
import library.csv
import library.comment
import library.file

import sys

source_path = app.settings["last_fm"]["source"]
compressed_path = app.settings["last_fm"]["compressed"]
track_database = app.settings["track_database"]

original_track_list = app.settings["karaokeversion"]["compressed"]

#######################################################

def create_profile_list():
    return_artist_profile = library.json.import_json(original_track_list)

    array = []
    for data in library.csv.import_csv(compressed_path):
        if data[0] != "artist" and data[1] != "track":
            for schema in return_artist_profile:
                if data[1] == schema["track"] and data[0] == schema["artist"]:
                    array.append({
                        "artist": schema["artist"],
                        "track": schema["track"],
                        "url": schema["url"],
                        "filename_artist": schema["filename_artist"],
                        "filename_track": schema["filename_track"],
                        "filename": schema["filename_artist"]+"-"+schema["filename_track"]
                    })
                else:
                    pass
    library.json.export_json(track_database, array)


def compile_list():
    array = []

    for data in library.scan.import_json_from_directory_recursively_items(source_path+"*.json"):

        for schema in data["data"]:

            if schema != "track":
                try:
                    schema["name"]
                except:
                    pass
                else:

                    if int(schema["playcount"]) >= 100000:
                        array.append({
                            "artist": schema["artist"]["name"],
                            "track": schema["name"],
                            "listeners": schema["listeners"],
                            "playcount": schema["playcount"]
                        })

    library.csv.export_csv(compressed_path, ["artist", "track", "listeners", "playcount"], array)


library.comment.returnMessage("Start")
compile_list()
library.comment.returnMessage("Completed: "+compressed_path)
library.file.execute(compressed_path)
library.comment.returnMessage("Running Profile Creator")
create_profile_list()
library.comment.returnMessage("Completed")
