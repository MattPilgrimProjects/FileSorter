import app
import library
import library.file
import library.comment
import library.directory

array=[]

for schema in library.json.import_json(app.settings["live_database"]):
    
    return_data="Not Found"

    if library.file.file_exists(app.settings["midi_body_structure"]+schema["source"]+"//"+schema["track_id"]+".json"):
        return_data = library.json.import_json(app.settings["midi_body_structure"]+schema["source"]+"//"+schema["track_id"]+".json")

    if library.file.file_exists(app.settings["raw_key_signatures"]+schema["source"]+"//"+schema["track_id"]+".json"):
        return_key_data = library.json.import_json(app.settings["raw_key_signatures"]+schema["source"]+"//"+schema["track_id"]+".json")

    library.directory.create_recursive_directory(app.settings["live_api"]+schema["url"])

    library.json.export_json(app.settings["live_api"]+schema["url"]+"//profile.json",{
        "artist":schema['artist'],
        "track":schema['track'],
        "audio_data":return_data,
        "key_signature":return_key_data
    })
    library.comment.returnUpdateMessage("Completed:"+app.settings["live_api"]+schema["url"]+"//profile.json                                              ")

library.comment.returnMessage("---")
library.comment.returnMessage("Completed")