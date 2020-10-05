import app
import library.json
import library.file
import library.midi
import library.comment

for schema in library.json.import_json(app.settings["live_database"]):

    json_output = app.settings["raw_midi_to_json"]+schema["title"]+"\\"+ schema["track_id"] + ".json"
    midi_input =  app.settings["raw_midi_path"]+schema["title"]+"\\"+schema["track_id"] + ".mid"

    if library.file.file_does_not_exists(json_output):

        try:
            mid = library.midi.read_midi(midi_input)  
        except TypeError as error_message:
            library.comment.returnMessage(str(error_message) +" - "+ schema["track_id"])
            pass
        except EOFError as error_message:
            library.comment.returnMessage(str(error_message) +" - "+ schema["track_id"])
            pass
        except OSError as error_message:
            library.comment.returnMessage(str(error_message) +" - "+ schema["track_id"])
            pass
        except ValueError as error_message:
            library.comment.returnMessage(str(error_message) +" - "+ schema["track_id"])
            pass 
        except NameError as error_message:
            library.comment.returnMessage(str(error_message) +" - "+ schema["track_id"])
            pass      
        else:
            library.json.export_json(json_output,mid)
            library.comment.returnMessage("Completed => "+json_output)