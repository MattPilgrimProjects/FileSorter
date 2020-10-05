import app
import library.scan
import library.json
import library.comment

array=[]
unclean=[]

live_database = app.settings["live_database"]

title=""
track_id=""

library.comment.returnMessage("Starting")

for schema in library.json.import_json(app.settings["database"]):

    for array_content in library.json.import_json(app.settings["search_database"]):

        if schema["track"] in array_content:

            if "freemidi" in array_content:
                title = "freemidi"
                track_id = array_content.split("-")[0]

            array.append({
                "title":title,
                "track_id":track_id,
                "artist": schema["artist"],
                "track": schema["track"],
                "url": schema["url"]
            })

            library.comment.returnUpdateMessage("Clean Data Added")

  
library.json.export_json("Z:\\raw_href\\unclean.json",unclean)
library.json.export_json(live_database,array)
library.comment.returnMessage("Completed: "+live_database)
