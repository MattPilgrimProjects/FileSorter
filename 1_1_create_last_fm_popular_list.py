import app
import config
import library.json
import library.scan
import library.csv
import library.comment
import library.file
import library.machine_learning

import sys

source_path = app.settings["last_fm"]["source"]
compressed_path = app.settings["last_fm"]["compressed"]
track_database = app.settings["track_database"]

original_track_list = app.settings["karaokeversion"]["compressed"]

#######################################################

def compress_api_data(input_filepath,export_file):

    array=[]
    
    for data in library.scan.import_json_from_directory_recursively_items(input_filepath):
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

    library.comment.returnMessage(export_file)
    return library.json.export_json(export_file,array)

def run_matching_algorithm(import_file,export_filepath_location):
    ## Run this second
    for original_data in library.json.import_json(original_track_list):

        filename= original_data["filename_artist"]+"-"+original_data["filename_track"]

        if library.file.file_does_not_exists(export_filepath_location+filename+".json"):

            last_fm_check_list=[]

            for schema in library.json.import_json(import_file):

                match_artist = library.machine_learning.match_by_percentage(original_data["artist"],schema["artist"])
                match_track = library.machine_learning.match_by_percentage(original_data["track"],schema["track"])


                if match_artist >=75 and match_track >=75:

                    last_fm_check_list.append({
                        "artist":schema["artist"],
                        "track":schema["track"],
                        "listeners":schema["listeners"],
                        "playcount":schema["playcount"],
                        "tags":schema["tags"],
                        "match_percentage":{
                            "artist":match_artist,
                            "track":match_track
                        }

                    })
            
            original_data["filename"] = filename

            
            library.json.export_json(export_filepath_location+original_data["filename"]+".json",{
                "original":original_data,
                "last_fm_check":last_fm_check_list
                })
            library.comment.returnUpdateMessage("Processing")
            
        else:
            pass

def run_processed_algorithm(import_filepath_location,export_filepath_location):
    for filename in library.scan.scan_file_recursively(import_filepath_location):

        for title,filedata in library.json.import_json(filename).items():

            if title=="original":
                original = filedata

            if title=="last_fm_check":
                for data in filedata:
                    if data["match_percentage"]["artist"]==100.0 and data["match_percentage"]["track"]==100.0:

                        if library.file.file_does_not_exists(export_filepath_location+original["filename"]+".json"):

                            library.json.export_json(
                                export_filepath_location+original["filename"]+".json",
                                [
                                    {
                                    "artist":original["artist"],
                                    "track":original["track"],
                                    "url":original["url"],
                                    "filename_artist":original["filename_artist"],
                                    "filename_track":original["filename_track"],
                                    "filename":original["filename"],
                                    "last_fm":{
                                        "last_fm_artist_match":data["artist"],
                                        "last_fm_track_match":data["track"],
                                        "listeners":data["listeners"],
                                        "playcount":data["playcount"],
                                        "tags":data["tags"]
                                    }
                                    }
                                
                                ])
             
def export_full_list(input_filepath_location,export_file):
    array=[]
    for filename in library.scan.scan_file_recursively("S:\\Midi-Library\\parsed\\matched\\processed\\*.json"):
        for filedata in library.json.import_json(filename):
            array.append(filedata)
    return library.json.export_json("S:\\Midi-Library\\parsed\\matched\\full_list.json",array)


def compressed_list(input_file,export_file):
    array=[]
    for filedata in library.json.import_json(input_file):
        if int(filedata["last_fm"]["playcount"]) >= 100000:

            array.append(config.import_html_content(filedata))

    return_dictionary = library.parser.remove_duplicates_from_dictionary(array)
    print("Number of Artists: "+str(len(return_dictionary)))

    return library.json.export_json(export_file,return_dictionary)
    

#######################################################

library.comment.returnMessage("Start")

compress_api_data("S:\\Website Projects\\live\\last_fm_tracks\\*.json","S:\\Midi-Library\\parsed\\uncompressed.json")
run_matching_algorithm("S:\\Midi-Library\\parsed\\uncompressed.json","S:\\Midi-Library\\parsed\\matched\\unprocessed\\")
run_processed_algorithm("S:\\Midi-Library\\parsed\\matched\\unprocessed\\*.json","S:\\Midi-Library\\parsed\\matched\\processed\\")
export_full_list("S:\\Midi-Library\\parsed\\matched\\processed\\*.json","S:\\Midi-Library\\parsed\\matched\\full_list.json")
compressed_list("S:\\Midi-Library\\parsed\\matched\\full_list.json","S:\\Midi-Library\\parsed\\matched\\compressed_list.json")
library.comment.returnMessage("Completed")