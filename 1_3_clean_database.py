import app
import re

def midiworld(schema):

        

        track = schema.split(" (")[0]

        artist = schema.replace(track+" (","").split(")")[0]

        url = "/"+artist.replace(" ","-").lower()+"/"+track.replace(" ","-").lower()

        track_id = schema.replace(" ("+artist+") - ","").replace(" =midiworld","").replace(track,"")

        return{
        "title":"midiworld",
        "track_id":track_id,
        "url": url,
        }


def freemidi(schema):

    schema = schema.replace("=freemidi","").lower()

    track_id = schema.split("-")[0]

    track = schema.split(" ")[0].replace(track_id+"-","")
    
    track = schema.replace(track,"").replace(track_id+"- ","").strip().replace(" ","-")

    artist = schema.split(" ")[0].replace(track_id+"-","").replace(track+"-","")

    return{
        "title":"freemidi",
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

for schema in app.json.import_json(app.settings["database"]):
   
    array_content = app.json.import_json(app.settings["search_database"])

    for array_value in array_content:     

        freemidi_group = freemidi(array_value) 
        midiworld_group = midiworld(array_value)

        if "=freemidi" in array_value and freemidi_group["url"] == schema["url"] and freemidi_group["track_id"].isdigit():
            clean_array.append(freemidi_group)  
            key.append(array_value)
            

        if "=midiworld" in array_value and midiworld_group["url"] == schema["url"] and midiworld_group["track_id"].isdigit():
            clean_array.append(midiworld_group)
            key.append(array_value)

        if "=freemidi" in array_value and freemidi_group["track_id"].isdigit():

            split_url = midiworld_group["url"].replace("/","-").split("-")

            stats = app.parser.match_percentage(split_url,schema["url"])

            if stats > 60:
                manual_search.append({
                    "track_id":freemidi_group["track_id"],
                    "url":freemidi_group["url"],
                    "match":schema["url"],
                    "stats":stats,
                    "schema":schema
                })

        if "=midiworld" in array_value and freemidi_group["track_id"].isdigit():


            stats = app.parser.match_percentage(
                midiworld_group["url"].replace("/","-").split("-"),
                schema["url"].replace("/","-").split("-")
                )

            if stats > 60:
                manual_search.append({
                    "track_id":freemidi_group["track_id"],
                    "url":freemidi_group["url"],
                    "match":schema["url"],
                    "stats":stats,
                    "schema":schema
                })
            
            pass

app.json.export_json(live_database,clean_array)

app.json.export_json("Z:\\raw_href\\processed.json",key)

app.json.export_json("Z:\\raw_href\\error.json",manual_search)

app.comment.returnMessage("Completed: "+live_database)