import app
import library.scan
import library.json
import library.parser
import library.comment
import library.file

for setting in app.settings['stage']:

    for filename in library.scan.scan_file_recursively(setting['raw_artist_match']+"*"):

        for schema in library.json.import_json(filename):

            raw_midi_path = setting["import_midi"]["download_location"]
            import_midi_url = setting["import_midi"]["download_url"]

            if library.file.file_does_not_exists(raw_midi_path+schema['track_id']+".mid"):

                midi = library.parser.request_data_from_url(import_midi_url+schema['track_id'])
                library.file.createFile(raw_midi_path+schema["track_id"]+".mid",midi.content)
                library.comment.returnMessage("Adding Song: " + raw_midi_path+schema['track_id']+".mid")

