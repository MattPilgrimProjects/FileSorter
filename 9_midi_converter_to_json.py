import app

for schema in app.json.import_json(app.settings["live_database"]):

    json_output = app.settings["raw_midi_to_json"]+schema["title"]+"\\"+ schema["track_id"] + ".json"
    midi_input =  app.settings["raw_midi_path"]+schema["title"]+"\\"+schema["track_id"] + ".mid"

    if app.file.file_exists(midi_input) and app.file.file_does_not_exists(json_output):

        app.comment.returnMessage("Processing => "+midi_input)

        midi_data = app.midi.return_notes_and_channels(midi_input,schema)

        app.json.export_json(json_output,midi_data)

        app.comment.returnMessage("Completed => "+json_output)
    else:
        app.comment.returnMessage("Already Added")
        pass