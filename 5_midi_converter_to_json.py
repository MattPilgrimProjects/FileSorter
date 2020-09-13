from app import setup
from app import app_setup
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

    midi_filename = app_setup(2)["storage"]["midi_library"]+track_details["track_id"]+".mid"

    process_filename = app_setup(2)['processing']["json_processed_path"]+track_details["track_id"]+".json"

    raw_filename = app_setup(2)['processing']["midi_processed_path"]

    if file_exists(process_filename) or file_exists(process_filename):
        pass
    else:
        try:
            mid = MidiFile(midi_filename)  
        except TypeError:
            print("TypeError - " + track_details["track_id"])
        except EOFError:
            print("EOFError - " +track_details["track_id"])
        except OSError:
            print("OSError - " +track_details["track_id"])
        else:
            array = library.midi.export_processed_content(mid,process_filename)
            library.json.export_json(process_filename,array)
            library.filemodels.move_file_content(midi_filename,raw_filename)
     
