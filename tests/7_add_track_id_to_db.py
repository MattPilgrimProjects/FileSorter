import app
import library.json
import library.comment

##################################################################

array=[]
freemidi=""
midiworld=""

for schema  in library.json.import_json(app.settings["database"]):

    for body  in library.json.import_json(app.settings["live_database"]):

        if schema['artist'] == body['artist'] and schema['track'] == body['track']:

            if body["title"]=="freemidi":
                library.comment.returnMessage(body["track_id"])
                freemidi=body["track_id"]   
            else:
                freemidi="not found"
                pass 

            if body["title"]=="midiworld":
                library.comment.returnMessage(body["track_id"])
                midiworld=body["track_id"]   
            else:
                midiworld="not found"
                pass
   
                schema["track_id"]={
                        "midiworld":midiworld,
                        "freemidi":freemidi
                }
            array.append(schema)

    pass

library.json.export_json(app.settings["database"],array)


# B07H625JJL&asins=B07H625JJL&linkId=f9eaaf4a9a59fa2db6e2dacb95621bef
# B084XTBW5H&asins=B084XTBW5H&linkId=144276f34ef9cd06b03b94ee14f011f0

# B00Y7PHI5Y


