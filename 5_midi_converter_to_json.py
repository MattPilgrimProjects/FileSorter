from mido import MidiFile
import library.tb
import library.json
import library.midi
import json
import library.filemodels


from library.json import import_json
######

tb = library.tb

setup = import_json("setup.json")

# Parse Midi Data to JSON Files

for track_details in import_json(setup["track_database"]):

    midi_filename = setup["midi_library_location"]+track_details["track_id"]+".mid"

    process_filename = setup['midi_library_location']+"processed\\"+track_details["track_id"]+".json"

    raw_filename = setup['midi_library_location']+"raw\\"

    if library.tb.file_does_not_exists(process_filename):

        try:
            mid = MidiFile(midi_filename)  
        except TypeError:
            print("TypeError")
        except EOFError:
            print("EOFError")
        except OSError:
            print("OSError")
        else:
            library.midi.export_processed_content(mid,process_filename)
            library.filemodels.move_file_content(midi_filename,raw_filename)
    else:
        pass


       
     
