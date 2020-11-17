import app

import library.midi
import library.comment
import library.scan
import library.file
import library.parser

#############################################################################

library.comment.returnMessage("Start")

for filename in library.scan.scan_file_recursively(app.midi_library_path+"*.mid"):

    track_id = library.parser.return_filename(filename,app.midi_library_path,".mid")
  
    json_output = app.midi_processed_path+track_id+".json"

    if library.file.file_exists(filename) and library.file.file_does_not_exists(json_output):

        midi_data = library.midi.return_notes_and_channels(filename)

        library.json.export_json(json_output,midi_data)

        library.comment.returnMessage("Converting " + json_output)
     
    else:
        pass

library.comment.returnMessage("Completed ")