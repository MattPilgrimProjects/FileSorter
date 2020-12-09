import app
import library.scan
import library.json
import library.file
import library.comment
import library.csv

def export_data_single(filename):
    library.comment.returnUpdateMessage("Processing " + filename)

    data = library.json.import_json(filename)

    json_data = []

    for schema in data["tracks"]["items"]:

        json_data.append({
            "href": schema["external_urls"]["spotify"]+"?highlight="+schema["uri"],
            "img":"https://www.scdn.co/i/_global/touch-icon-114.png",
            "embed":"https://open.spotify.com/embed/track/"+schema["uri"].replace("spotify:track:","")
        })

        pass

    try:
        json_data[0]
    except:
        output = {}
    else:
        output = json_data[0]

    return output

library.comment.returnMessage("Start")

for filename in library.scan.scan_file_recursively(app.settings["spotify"]["export"]+"*.json"):

    return_filename = filename.replace(
        app.settings["spotify"]["export"], "")

    # if library.file.file_exists(app.settings["spotify"]["track_list"]+return_filename):
    #     pass
    # else:
    export = export_data_single(filename)
    library.json.export_json(app.settings["spotify"]["track_list"]+return_filename,export)
    
library.comment.returnMessage("---------")

library.comment.returnMessage("Completed")
