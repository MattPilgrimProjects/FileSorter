import app
import library.file
import library.csv
import library.json
import library.cron
import library.url
import library.comment
import library.scan

import sys

track_database = app.settings["track_database"]
source_path = app.settings["youtube"]["source"]
auth = app.settings["youtube"]["auth"]
api_key = app.settings["youtube"]["api"]

for data in library.json.import_json(track_database):

    filename = data["filename"]+".json"
    artist = data["artist"]
    track = data["track"]

    if library.file.file_exists(source_path+filename):
        pass
    else:
        params = (
                ('q', artist+" "+track),
                ('part', 'snippet'),
                ('key', api_key)
            )
        library.cron.delay(2)
        library.comment.returnMessage("Processing "+source_path+filename)
        content = library.url.youtube_web_api(params,auth)
        library.json.export_json(source_path+filename,content)
        library.comment.returnMessage("Added "+source_path+filename)
