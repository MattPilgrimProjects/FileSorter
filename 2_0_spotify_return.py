import app
import library.file
import library.json
import library.cron
import library.url
import library.comment
import library.scan
import sys

track_database = app.settings["track_database"]
export_path = app.settings["spotify"]["export"]

print("Enter the auth token:")
auth = "Bearer "+input()

for data in library.json.import_json(track_database):
    artist = data["artist"]
    track = data["track"]

    filepath = export_path+data["filename"]+".json"

    if library.file.file_does_not_exists(filepath):
        params = (
            ('q', artist+" "+track),
            ('type', 'track,artist'),
            ('limit', '20'),
            ('market', 'US'),
            ('include_external', 'audio')
        )
        content = library.url.spotify_web_api("https://api.spotify.com/v1/search",params,auth)
        library.json.export_json(filepath,content)
        library.comment.returnUpdateMessage("Added: "+filepath)

library.comment.returnMessage("Completed")