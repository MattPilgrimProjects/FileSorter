import app
import library.json
import library.comment

search_database = app.settings["search_database"]

search_database = library.json.import_json(search_database)

live_database = app.settings["live_database"]

array=[]

def freemidi(schema):

    track_id = schema.replace("a href=download3-","").split("-")[0]

    track = schema.split("=")[2]

    artist_lower_case = track.replace(" ","-").lower()

    artist = schema.replace("a href=download3-","").replace(artist_lower_case,"").replace(track_id,"").split("title=")[0].replace("--","").title().replace("-"," ")

    return{
        "track_id":track_id,
        "artist":artist,
        "track":track
        }

def midiworld(schema):

        return{
        "track_id":schema.split(" - ")[1].replace('\" ',"").replace("a href=httpswwwmidiworldcomdownload",""),
        "artist":schema.split("(")[1].split(")")[0],
        "track":schema.split(" (")[0]
        }




for schema in search_database:

    if schema['title']=="freemidi":group = freemidi(schema['raw']) 

    if schema['title']=="midiworld":group = midiworld(schema['raw'])  

    if group["track_id"].strip().isdigit():


        array.append({
            "title":schema["title"].strip(),
            "track_id":group["track_id"].strip(),
            "artist":group["artist"].strip(),
            "track":group["track"].strip()
        })

    else:
        pass

library.json.export_json(live_database,array)
library.comment.returnMessage("Completed: "+live_database)

