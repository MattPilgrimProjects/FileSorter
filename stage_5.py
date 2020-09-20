import app
import library.json
import library.directory

live_database = app.setup["live_database"]

live_app = app.setup["live_api"]

live_database = library.json.import_json(live_database)

for schema in live_database:
    filepath = live_app+schema['artist'].lower().replace(" ","-")+"\\"+schema['track'].lower().replace(" ","-").replace(",","").replace("'","")
    filename = schema["track_id"]+".json"

    library.directory.create_recursive_diretory(filepath)
    library.json.export_json(filepath+"\\"+filename,{
        "Artist":schema["artist"],
        "Track":schema["track"]
    })

    pass

