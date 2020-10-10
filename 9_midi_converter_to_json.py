import app

for schema in app.json.import_json(app.settings["live_database"]):

    json_output = app.settings["raw_midi_to_json"]+schema["title"]+"\\"+ schema["track_id"] + ".json"
    midi_input =  app.settings["raw_midi_path"]+schema["title"]+"\\"+schema["track_id"] + ".mid"

    if app.file.file_does_not_exists(json_output):

        try:
            mid = app.midi.read_midi(midi_input)  
        except TypeError as error_message:
            app.comment.returnMessage(str(error_message) +" - "+ schema["track_id"])
            pass
        except EOFError as error_message:
            app.comment.returnMessage(str(error_message) +" - "+ schema["track_id"])
            pass
        except OSError as error_message:
            app.comment.returnMessage(str(error_message) +" - "+ schema["track_id"])
            pass
        except ValueError as error_message:
            app.comment.returnMessage(str(error_message) +" - "+ schema["track_id"])
            pass 
        except NameError as error_message:
            app.comment.returnMessage(str(error_message) +" - "+ schema["track_id"])
            pass      
        else:
            app.directory.create_recursive_diretory(app.settings["live_api"]+schema['url'])
            app.json.export_json(json_output,mid)
            app.comment.returnMessage("Completed => "+json_output)