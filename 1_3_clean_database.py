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

array=[]

unclean=[]

live_database = app.settings["live_database"]

title=""

track_id=""

clean_array=[]

unclean_array=[]

app.comment.returnMessage("Starting")

key=[]

manual_search=[]

keyword = app.random_keyword()

for schema in app.json.import_json("Z:\\raw_api_keywords\\"+keyword+".json"):
   
    array_content = app.json.import_json("S:\\Midi-Library\\raw_keywords_json\\freemidi\\"+keyword+".json")

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
            
            pass

app.json.export_json("Z:\\raw_href\\"+keyword+".json",manual_search)

app.comment.returnMessage("Completed: "+"Z:\\raw_href\\"+keyword+".json")