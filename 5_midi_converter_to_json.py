from app import setup
from mido import MidiFile
import library.tb
import library.json
import library.midi
import json
import library.filemodels


from library.json import import_json
from library.tb import file_exists
######

tb = library.tb


# Parse Midi Data to JSON Files

for track_details in import_json(setup["track_database"]):

    midi_filename = setup["midi_library_location"]["download_path"]+track_details["track_id"]+".mid"

    process_filename = setup['midi_library_location']["json_processed_path"]+track_details["track_id"]+".json"

    raw_filename = setup['midi_library_location']["midi_processed_path"]

    if file_exists(process_filename) or file_exists(process_filename):
        pass
    else:
        try:
            mid = MidiFile(midi_filename)  
        except TypeError:
            print("TypeError")
        except EOFError:
            print("EOFError")
        except OSError:
            print("OSError")
        else:
            array = library.midi.export_processed_content(mid,process_filename)
            library.json.export_json(process_filename,array)
            library.filemodels.move_file_content(midi_filename,raw_filename)
     
