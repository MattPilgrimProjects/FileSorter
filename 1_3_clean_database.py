import app
# import re
import library

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

def clear_database():

    manual_search=[]

    for schema in library.json.import_json(app.settings["sources"]["track_list"]["json"]):

        array_content = app.json.import_json(app.settings["sources"]["midi_list"]["json"])

        for array_value in array_content:
        
            if "=>freemidi" in array_value:
                group = freemidi(array_value,schema)
            else:
                group= midiworld(array_value,schema)            

            if group["track_id"].isdigit():

                split_url = group["url"].replace("/","-").split("-")

                stats = app.parser.match_percentage(split_url,schema["url"])

            if stats > 90:

                library.comment.returnUpdateMessage("Added:"+ schema["url"]+"                                              ")
                manual_search.append({
                    "url_artist":schema["url"].split("/")[1],
                    "url_track":schema["url"].split("/")[2],
                    "source":group["source"],
                    "artist":group["artist"],
                    "track":group["track"],
                    "track_id":group["track_id"],
                    "check_url":group["url"],
                    "original_url":schema["url"],
                    "stats":stats
                })
    return None

app.comment.returnMessage("Start")
app.json.export_json(app.settings["sources"]["midi_list_tidy"]["json"],clear_database())
app.csv.export_csv(app.settings["sources"]["midi_list_tidy"]["csv"],["source","artist","track","track_id","check_url","original_url","stats"],clear_database())
app.comment.returnMessage("Completed")