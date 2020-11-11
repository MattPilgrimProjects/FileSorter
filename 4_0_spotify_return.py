import app
import library.file
import library.csv
import library.json
import library.cron
import library.url
import library.comment

import sys

def create_filename(csv_row):

    return csv_row[1:].replace("/","-")+".json"

print("Enter the auth token:")
auth = "Bearer "+input()

for row in library.json.import_json("S:\\Midi-Library\\sources\\track_list.json"):

    artist = row["artist"] 
    track = row["track"]
    url = row["url"]

    filename = app.settings["spotify"]["export"]+create_filename(url)

    if library.file.file_exists(filename):
        pass
    else:
        library.comment.returnMessage("Processing "+filename)

        params = (
            ('q', artist+" "+track),
            ('type', 'track,artist'),
            ('limit', '20'),
            ('market','US'),
            ('include_external','audio')
        )
        library.cron.delay(5)
        content = library.url.spotify_web_api(params,auth)
        if content:
            library.json.export_json(filename,content)
            library.comment.returnMessage("Added "+filename)
        else:
            sys.exit()


        