import app
# import re
import library
import time

# This is significantly longer to run so ideally run at midnight (takes around 2 hours to compile)

def midiworld(schema,data):

        track = schema.split(" (")[0]

        artist = schema.replace(track+" (","").split(")")[0]

        url = "/"+artist.replace(" ","-").lower()+"/"+track.replace(" ","-").lower()

        track_id = schema.replace(" ("+artist+") - ","").replace("=>midiworld","").replace(track,"")

        return{
        "artist":data["artist"],
        "track":data["track"],
        "source":"midiworld",
        "track_id":track_id,
        "url": url,
        }

def freemidi(schema,data):

    schema = schema.replace("=>freemidi","").lower()

    track_id = schema.split("-")[0]

    track = schema.split(" ")[0].replace(track_id+"-","")
    
    track = schema.replace(track,"").replace(track_id+"- ","").strip().replace(" ","-")

    artist = schema.split(" ")[0].replace(track_id+"-","").replace(track+"-","")

    return{
        "artist":data["artist"],
        "track":data["track"],
        "source":"freemidi",
        "track_id":track_id,
        "url": "/"+artist+"/"+track
        }

def clear_database(track_list,midi_list):

    manual_search=[]

    for schema in library.json.import_json(track_list):

        array_content = app.csv.importCSVData(midi_list)

        for array_value in array_content:

            array_value = array_value[0]

                    
            if "=>freemidi" in array_value: 
                group = freemidi(array_value,schema)
            else:
                group = midiworld(array_value,schema)  
            

            if group["track_id"].isdigit():

                split_url = group["url"].replace("/","-").split("-")

                stats = app.parser.match_percentage(split_url,schema["url"])

                if stats >= 92:

                    manual_search.append({
                            "source":group["source"],
                            "artist":group["artist"],
                            "track":group["track"],
                            "track_id":group["track_id"],
                            "check_url":group["url"],
                            "original_url":schema["url"],
                            "stats":stats
                    })
                   
               


    return manual_search


library.comment.returnMessage("Start")
for track_list in library.scan.scan_file_recursively(app.settings["api"][0]["parsed_data"]["json"]+"*.json"):

    keyword = library.parser.find_and_replace_array(track_list,{
        app.settings["api"][0]["parsed_data"]["json"]:"",
        ".json":""
    })
        
    for schema in app.settings["stage"]:

        track_list = app.settings["api"][0]["parsed_data"]["json"]+keyword+".json"

        midi_list = schema["keywords"]["output"]["csv"]+keyword+".csv"

        if library.file.file_exists(track_list) and library.file.file_exists(midi_list) and library.file.file_does_not_exists(schema["track_to_midi"]["output"]["csv"]+keyword+".csv"):

            app.csv.export_csv(schema["track_to_midi"]["output"]["csv"]+keyword+".csv",["source","artist","track","track_id","check_url","original_url","stats"],clear_database(track_list,midi_list))
            
            library.comment.returnUpdateMessage("Completed " + schema["track_to_midi"]["output"]["csv"]+keyword+".csv                                       ")
        else:
            pass
 

        pass
library.comment.returnMessage("Completed")