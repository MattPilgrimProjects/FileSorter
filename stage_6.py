import app
import library.json
import library.directory
import library.file
import library.comment
import library.parser


live_database = app.setup["live_database"]

raw_midi_path = app.setup["raw_midi_path"]

live_database = library.json.import_json(live_database)

for schema in live_database:

    title = schema["title"]

    if library.file.file_does_not_exists(raw_midi_path+title+"\\"+schema["track_id"]+".mid") and int(schema["track_id"]) < 500:

        midi = library.parser.request_data_from_url(app.setup["import_midi_url"][title]+schema["track_id"])
        library.file.createFile(raw_midi_path+title+"\\"+schema["track_id"]+".mid",midi.content)
        library.comment.returnMessage("Adding Song: " + raw_midi_path+title+"\\"+schema["track_id"]+".mid")

    else:
        library.comment.returnMessage("Completed Song: " + raw_midi_path+title+"\\"+schema["track_id"]+".mid")
        pass
        



