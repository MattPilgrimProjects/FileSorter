import app
import re

def midiworld(schema,data):

        track = schema.split(" (")[0]

        artist = schema.replace(track+" (","").split(")")[0]

        url = "/"+artist.replace(" ","-").lower()+"/"+track.replace(" ","-").lower()

        track_id = schema.replace(" ("+artist+") - ","").replace(" =>midiworld","").replace(track,"")

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

def return_keywords_from_processed_list(schema):

    keyword_array = []

    for filename in app.scan.scan_file_recursively(schema["raw_keywords_json"]+"\\*"):

        keyword = app.parser.find_and_replace_array(filename,{
           schema["raw_keywords_json"]:"",
            ".json":""
        })

        keyword_array.append(keyword)

    return keyword_array


for setting in app.setup['stage']:

    for keyword in return_keywords_from_processed_list(setting):

        array_content = app.json.import_json(setting["raw_keywords_json"]+keyword+".json")

        if app.file.file_exists(app.setup['raw_api_keywords']+keyword+".json"):

            manual_search=[]

            for schema in app.json.import_json(app.setup['raw_api_keywords']+keyword+".json"):
    
                for array_value in array_content:

                    freemidi_group = freemidi(array_value,schema) 

                    midiworld_group = midiworld(array_value,schema)

                    if "=>freemidi" in array_value and freemidi_group["track_id"].isdigit():

                        split_url = midiworld_group["url"].replace("/","-").split("-")

                        stats = app.parser.match_percentage(split_url,schema["url"])

                        if stats > 80:
                            manual_search.append({
                                "source":freemidi_group["source"],
                                "track_id":freemidi_group["track_id"],
                                "url":freemidi_group["url"],
                                "match":schema["url"],
                                "stats":stats,
                                "schema":schema
                            })

                    if "=>midiworld" in array_value and freemidi_group["track_id"].isdigit():

                        stats = app.parser.match_percentage(
                            midiworld_group["url"],
                            schema["url"]
                            )

                        if stats > 80:
                            manual_search.append({
                                "source":midiworld_group["source"],
                                "track_id":midiworld_group["track_id"],
                                "url":midiworld_group["url"],
                                "match":schema["url"],
                                "stats":stats,
                                "schema":schema
                            })

            if manual_search !=[]:

                app.json.export_json("S:\\Midi-Library\\raw_artist_match\\"+keyword+".json",manual_search)
                app.comment.returnMessage("Completed: "+"S:\\Midi-Library\\raw_artist_match\\"+keyword+".json")

      
                    
            

        else:
            pass


  
 



