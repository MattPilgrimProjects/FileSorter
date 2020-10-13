import app
import library.scan
import library.midi
import library.parser

for setting in app.setup['stage']:

    for filename in library.scan.scan_file_recursively(setting["import_midi"]["download_location"]+"*"):

        track_id = library.parser.find_and_replace_array(filename,{
            setting["import_midi"]["download_location"]:"",
            ".mid":""
        })
        
        json_output = setting['raw_midi_to_json']+track_id+".json"

        app.comment.returnMessage("Processing => "+filename)

        midi_data = library.midi.return_notes_and_channels(filename,track_id)

        app.json.export_json(json_output,midi_data)

        app.comment.returnMessage("Completed => "+json_output)
