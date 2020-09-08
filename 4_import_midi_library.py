from app import setup

import requests
from library.json import import_json
from library.tb import file_does_not_exists
from library.tb import file_exists
import library.tb

return_midi_list = setup['json_local_midi_library']['freemidi']

# Be VERY careful when using this

for uri in import_json(return_midi_list)['tracks']:

    midi_id = uri.split("-")[1]

    download_path = setup['midi_library_location']["download_path"]+midi_id+'.mid'
    midi_processed_path = setup['midi_library_location']["midi_processed_path"]+midi_id+'.mid'
    json_processed_path = setup['midi_library_location']["json_processed_path"]+midi_id+'.json'

    if file_exists(midi_processed_path) or file_exists(download_path) or file_exists(json_processed_path):
        pass
    else:
        # midi = requests.get(setup["midi_library_public_link"]["freemidi"]+midi_id, allow_redirects=False)
        # open(setup['midi_library_location']["download_path"]+midi_id+'.mid', 'wb').write(midi.content)
        library.tb.returnMessage("Adding Song")

