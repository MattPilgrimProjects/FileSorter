import app

import library.midi
import library.comment
import library.scan
import library.file

channel_name  = library.json.import_json("S:\\Midi-Library\\instruments.json")

library.comment.returnMessage("Start")

for setting in app.setup['stage']:

    for filename in library.scan.scan_file_recursively(setting["import_midi"]["download_location"]+"*.mid"):

        track_id = library.parser.find_and_replace_array(filename,{
            setting["import_midi"]["download_location"]:"",
            ".mid":""
        })
        
        json_output = setting['raw_midi_to_json']+track_id+".json"

        if library.file.file_exists(filename) and library.file.file_does_not_exists(json_output):

            midi_data = library.midi.return_notes_and_channels(filename,track_id,channel_name)

            library.json.export_json(json_output,midi_data)

            library.comment.returnMessage("Converting " + json_output)
     
        else:
            pass

library.comment.returnMessage("Completed ")