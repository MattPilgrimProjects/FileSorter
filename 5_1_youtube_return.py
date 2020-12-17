import app
import config
import library.json
import library.download

track_database =app.settings["main_database_file"]

youtube_library = "S:\\Midi-Library\\url\\youtube_library.json"

export_list = []

for data in library.json.import_json(track_database):

    export_list.append(config.youtube_handler(data))

library.json.export_json(youtube_library, export_list)

library.comment.returnMessage("Start")
library.download.download_youtube(youtube_library)
library.comment.returnMessage("Completed")