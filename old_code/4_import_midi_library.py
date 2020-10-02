from app import setup
from app import app_setup

import requests
from library.json import import_json
from library.tb import file_does_not_exists
from library.tb import file_exists
import library.tb

return_midi_list =app_setup(1)['storage']['search_results']

# Be VERY careful when using this

for uri in import_json(return_midi_list)['tracks']:

    midi_id = uri.split("-")[1]

    download_path = app_setup(1)['storage']['midi_library']+midi_id+'.mid'
    midi_processed_path = app_setup(1)['processing']["midi_processing_path"]+midi_id+'.mid'
    json_processed_path = app_setup(1)['processing']["json_processing_path"]+midi_id+'.json'

    if file_exists(midi_processed_path):
        pass
    elif file_exists(download_path):
        pass
    elif file_exists(json_processed_path):
        pass
    else:
        midi = requests.get(app_setup(1)["download_link"]+midi_id, allow_redirects=False)
        open(app_setup(1)["storage"]["midi_library"]+midi_id+'.mid', 'wb').write(midi.content)
        library.tb.returnMessage("Adding Song: " + midi_id)

