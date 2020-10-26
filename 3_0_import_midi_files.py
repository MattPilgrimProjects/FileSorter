import app
import library.scan
import library.json
import library.parser
import library.comment
import library.file

import time

def import_midi_files(schema):

    if library.file.file_exists(app.settings["sources"]["midi_location"]+schema["source"]+"\\"+schema["track_id"]+".mid"):
        pass
    else:
        midi = library.parser.request_data_from_url(app.settings["import_midi_url"][schema["source"]]+schema["track_id"])
        library.file.createFile(app.settings["sources"]["midi_location"]+schema["source"]+"\\"+schema["track_id"]+".mid",midi.content)


    return app.comment.returnMessage("Track Added: "+app.settings["sources"]["midi_location"]+schema["source"]+"\\"+schema["track_id"]+".mid")

for schema in library.json.import_json(app.settings["sources"]["midi_list_tidy"]["json"]):
    time.sleep(10)
    import_midi_files(schema)
