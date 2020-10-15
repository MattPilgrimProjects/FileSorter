import app
import library
import library.file

array=[]

for schema in library.json.import_json(app.settings["live_database"]):
    
    return_data="Not Found"

    if library.file.file_exists(app.settings["midi_body_structure"]+schema["source"]+"//"+schema["track_id"]+".json"):
        return_data = library.json.import_json(app.settings["midi_body_structure"]+schema["source"]+"//"+schema["track_id"]+".json")

    library.directory.create_recursive_diretory(app.settings["live_api"]+schema["url"])
    library.json.export_json(app.settings["live_api"]+schema["url"]+"//profile.json",{
        "artist":schema['artist'],
        "track":schema['track'],
        "audio_data":return_data
    })

    array.append({
        "artist":schema['artist'],
        "track":schema['track'],
        "url":schema["url"]
    })
    

library.json.export_json(app.settings["www"],array)