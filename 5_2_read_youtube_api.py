import app
import library.scan
import library.json
import library.file
import library.comment

source_path = app.settings["youtube"]["source"]

def export_data(filename, return_filename):
    library.comment.returnMessage("Processing " + filename)

    json_data = []

    for schema in data["items"]:

        try:
            schema["id"]["videoId"]
        except:
            videoId = ""
            vid=""
        else:
            videoId = "https://www.youtube.com/watch?v="+schema["id"]["videoId"]
            vid = schema["id"]["videoId"]

        json_data.append({
            "href": videoId,
            "img":"https://www.youtube.com/s/desktop/208916f9/img/favicon_96.png",
            "embed":"https://www.youtube.com/embed/"+vid

        })

        pass

    library.json.export_json(
        app.settings["youtube"]["track_list"]+return_filename, json_data[0])


for filename in library.scan.scan_file_recursively(source_path+"*.json"):

    data = library.json.import_json(filename)

    return_filename = filename.replace(source_path, "")

    # If exists, then write over existing content
    export_data(filename, return_filename)

    pass
