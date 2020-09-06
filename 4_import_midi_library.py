import requests
import library.json
import library.tb

setup = library.json.import_json("setup.json")

return_midi_list = library.json.import_json(setup['json_local_midi_library']['freemidi'])



for uri in return_midi_list['tracks']:

    midi_id = uri.split("-")[1]

    if library.tb.file_does_not_exists(setup['midi_library_location']+midi_id+'.mid'): 

        midi = requests.get(setup["midi_library_public_link"]["freemidi"]+midi_id, allow_redirects=False)
        open(setup['midi_library_location']+midi_id+'.mid', 'wb').write(midi.content)
        library.tb.returnMessage("Adding Song")
    else:
        library.tb.returnMessage("MIDI file exists")