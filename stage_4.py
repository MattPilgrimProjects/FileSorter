import app
import library.json
import library.comment

search_database = app.setup["search_database"]

search_database = library.json.import_json(search_database)

live_database = app.setup["live_database"]

array=[]

def freemidi(schema):
    data = schema.split(" ")
        
    track_id = schema.split("-")[0]

    raw = schema.replace(track_id+"-","")

    raw_1 = schema.split(" ")

    raw_2 = schema.replace(raw_1[0],"")

    split_track = raw_2.lower().replace(" ","-").split("-")
        
    split_track.pop(0)

    track_slash = "-".join(split_track)

    track = schema.replace(raw.split(" ")[0],"").replace(track_id,"").replace("- ","").replace('title=',"").title().strip()

    track_return = track.replace("(","").replace(")","")

    return{
        "track_id":schema.split("-")[0],
        "artist":schema.replace(track_slash,"").replace(track_id,"").split(" ")[0].replace("--","").title().replace("-"," ").replace(track_return,"").strip(),
        "track":track
        }

def midiworld(schema):

        return{
        "track_id":schema.split(" - ")[1].replace('\" ',""),
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


    pass

library.json.export_json(live_database,array)
library.comment.returnMessage(live_database)

