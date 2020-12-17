import app
import library.file
import library.json
import library.cron
import library.url
import library.comment
import library.scan
import sys

track_database = app.settings["track_database"]


def export_data(filename):

    data = library.json.import_json(filename)

    library.comment.returnUpdateMessage("Processing " + filename)

    json_data = []

    if data["tracks"]["items"]:
        artist = data["tracks"]["items"][0]["artists"][0]["name"]

        for schema in data["tracks"]["items"]:

            if schema["album"]["images"]:
                album_cover = schema["album"]["images"][0]["url"]
            else:
                album_cover = ""

            if artist == schema["album"]["artists"][0]["name"]:

                json_data.append({
                    "artist": schema["album"]["artists"][0]["name"],
                    "album": schema["album"]["name"],
                    "album_artwork": album_cover
                })
    return json_data


library.comment.returnMessage("Start")

for filename in library.scan.scan_file_recursively(app.settings["spotify"]["export"]+"*.json"):

    return_filename = filename.replace(
        app.settings["spotify"]["export"], "")

    if library.file.file_exists(app.settings["spotify"]["album_list"]+return_filename):
        pass
    else:
        export = export_data(filename)
        library.json.export_json(
            app.settings["spotify"]["album_list"]+return_filename, library.parser.compress_dictionary(export))

library.comment.returnMessage("---------")

library.comment.returnMessage("Completed")
