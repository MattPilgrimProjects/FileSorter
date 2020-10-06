import app
import library.json
import library.directory
import library.file
import library.comment
import library.parser
import library.midi

import time

database = app.setup["live_database"]

raw_midi_path = app.setup["raw_midi_to_json"]

database = library.json.import_json(database)

for schema in database:

    title = schema["title"]

    if int(schema['track_id']) == 2600:
        
        if library.file.file_does_not_exists(raw_midi_path+title+"\\"+schema['track_id']+".json"):

            midi = library.parser.request_data_from_url(app.setup["import_midi_url"][title]+schema['track_id'])
            library.file.createFile(raw_midi_path+title+"\\"+schema["track_id"]+".mid",midi.content)
            library.comment.returnMessage("Adding Song: " + raw_midi_path+title+"\\"+schema['track_id']+".mid")



