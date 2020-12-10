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

def return_list(value):
    array=[]
    for data in library.json.import_json(original_track_list):
        array.append(data[value])
    return library.parser.remove_duplicates_from_array(array)

artist_list = return_list("artist")
track_list = return_list("track")

def learning(single,array):
    return_array=[]
    for value in array:

        if single in value or single.title() in value:
            return_array.extend({
                value
            })

    return return_array

def artist_match(single,array):
    return_array=[]
    for value in array:

        est = library.parser.high_match_percentage(single,value)
        
        if  est >= 25:

            return_array.append({
                value:est,
            })
    return return_array
    
def clever_match_artist_to_track(artist_array,track_array):
    
    array=[]
    for data in library.json.import_json(original_track_list):
        if data["artist"] in artist_array and data["track"] in track_array:
            array.append(data)
    return array

def export_learning_results():
    return_json=[]
    for data  in library.json.import_json("S:\\Midi-Library\\parsed\\compressed.json"):


        match_to_artist = learning(data["artist"],artist_list)
        match_to_track = learning(data["track"],track_list)
        match_artist_to_track = clever_match_artist_to_track(match_to_artist,match_to_track)
            
        return_json.append({
                "artist":data["artist"],
                "track":data["track"],
                "tags":data["tags"],
                "clever_match_artist":match_to_artist,
                "clever_match_track":match_to_track,
                "clever_match_artist_to_track":match_artist_to_track
        })
        library.comment.returnMessage("Processing: "+data["artist"]+" "+data["track"])

    return library.json.export_json("S:\\Midi-Library\\sources\\learning.json",return_json)

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

                    if int(schema["playcount"]) >= 1000000:
                        library.comment.returnUpdateMessage("Adding: "+schema["artist"]["name"] +" - "+schema["name"])
                        array.append({
                            "artist": schema["artist"]["name"],
                            "track": schema["name"],
                            "listeners": schema["listeners"],
                            "playcount": schema["playcount"],
                            "tag_1":schema["tags"][0]["name"]
                        })

    library.csv.export_csv(
        compressed_path, ["artist", "track", "listeners", "playcount","tag_1"], array)

def export_array_handler(data,schema):
    return {
        "artist": schema["artist"],
        "track": schema["track"],
        "tags":schema["tags"],
        "url": data["url"],
        "filename_artist": data["filename_artist"],
        "filename_track": data["filename_track"],
        "filename":data["filename_artist"]+"-"+data["filename_track"],
        "affilate_match":{
            "artist":data["artist"],
            "track":data["track"]
        }
    }

def compress_api_data():

    array=[]
    
    for data in library.scan.import_json_from_directory_recursively_items(source_path+"*.json"):
        for schema in data["data"]: 

            artist=""
            track=""
            listeners=""
            playcount=""
            tags=[]

            try:
                schema["artist"]["name"]
                schema["name"]
                schema["listeners"]
                schema["playcount"]
                schema["toptags"]["tag"]
            except:
                pass
            else:
                artist = schema["artist"]["name"]
                track = schema["name"]
                listeners = schema["listeners"]
                playcount = schema["playcount"]
                tags=schema["toptags"]["tag"]

            result_tags=[]

            if tags:   
                for tag in tags:
                    result_tags.append(tag["name"])


            



            if listeners and playcount and track and artist and result_tags:

                array.append({
                    "artist":artist,
                    "track":track,
                    "listeners":listeners,
                    "playcount":playcount,
                    "tags":result_tags
                })

    library.json.export_json("S:\\Midi-Library\\parsed\\uncompressed.json",array)

def create_compressed_list():

    playcount_list=[]
    for data in library.json.import_json("S:\\Midi-Library\\parsed\\uncompressed.json"):
        playcount_list.append(int(data["playcount"]))
    
    playcount_list.sort()

    new_playcount=[]

    for counts  in playcount_list:

        if counts > 1000000:
            new_playcount.append(counts)
    
    compressed_dictionary=[]

    for schema  in library.json.import_json("S:\\Midi-Library\\parsed\\uncompressed.json"):

        if int(schema["playcount"]) in new_playcount:
            compressed_dictionary.append(schema)
    
    return library.json.export_json("S:\\Midi-Library\\parsed\\compressed.json",compressed_dictionary)

def export_sorted_by_popular():
    export=[]
    for data in library.json.import_json("S:\\Midi-Library\\sources\\learning.json"):

        match_array  = data["clever_match_artist_to_track"]

        if len(match_array) ==1:
            export.append(export_array_handler(match_array[0],data))
        elif len(match_array)>=1:
            for data_single in match_array:
                export.append(export_array_handler(data_single,data))
        else:
            pass
    library.json.export_json(track_database,export)
    library.comment.returnMessage("Completed: " + track_database)


library.comment.returnMessage("Start")
compress_api_data()
create_compressed_list()
export_learning_results()
export_sorted_by_popular()
library.comment.returnMessage("Completed")
