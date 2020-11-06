import app
import library.scan
import library.csv
import library.parser
import library.file
import library.comment

array=[]

library.comment.returnMessage("Start")

for filename in library.scan.scan_file_recursively(app.settings["live_api"]+"/*/*/profile.json"):

    match_url = filename.replace("\profile.json","").replace(app.settings["live_api"],"/").replace("\\","/")

    data = library.json.import_json(filename)

    array.append({
                "artist":data['artist'],
                "track":data['track'],
                "url":match_url,
                "url_artist":match_url.split("/")[1],
                "url_track":match_url.split("/")[2],

            })

library.json.export_json(app.settings["www"],array)
library.csv.export_csv("live_api.csv",["artist","track","url","url_artist","url_track"],array)
library.comment.returnMessage("Completed")
 