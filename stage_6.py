import app
import library.json
import library.directory
import library.file
import library.comment

import requests

live_database = app.setup["live_database"]

raw_midi_path = app.setup["raw_midi_path"]

live_database = library.json.import_json(live_database)

for schema in live_database:

    title = schema["title"]

    if library.file.file_does_not_exists(raw_midi_path+title+"\\"+schema["track_id"]+".mid"):

        midi = requests.get(app.setup["import_midi_url"][title]+schema["track_id"], allow_redirects=False)
        open(raw_midi_path+title+"\\"+schema["track_id"]+".mid", 'wb').write(midi.content)
        library.comment.returnMessage("Adding Song: " + schema["track_id"])


    else:
        library.comment.returnMessage("Completed Song: " + schema["track_id"])
        pass
        



