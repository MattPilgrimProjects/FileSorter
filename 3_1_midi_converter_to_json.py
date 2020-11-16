import app

import library.midi
import library.comment
import library.scan
import library.file

def return_filename(filename,filepath,file_extension):

    return library.parser.find_and_replace_array(filename,{
            filepath:"",
            file_extension:""
    })

#############################################################################

channel_name  = library.json.import_json("S:\\Midi-Library\\instruments.json")

library.comment.returnMessage("Start")

for filename in library.scan.scan_file_recursively("S:\\Midi-Library\\raw_midi\\freemidi\\processed\\"+"*.mid"):

    track_id = return_filename(filename,"S:\\Midi-Library\\raw_midi\\freemidi\\processed\\",".mid")
  
    json_output = "S:\\Midi-Library\\raw_midi\\freemidi\\processed\\json\\"+track_id+".json"

    if library.file.file_exists(filename) and library.file.file_does_not_exists(json_output):

        midi_data = library.midi.return_notes_and_channels(filename,channel_name)

        library.json.export_json(json_output,midi_data)
        library.comment.returnMessage("Converting " + json_output)
     
    else:
        pass

library.comment.returnMessage("Completed ")