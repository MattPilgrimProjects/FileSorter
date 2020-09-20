from app import setup
from app import app_setup
import app
import library.tb
import library.json

db=[]

for preset_title in setup['midi_library']:

    preset_json = setup['midi_library'][preset_title]["export"]["track_listing"]

    for body in app.import_config(preset_json):

        path = setup['live_database']+body['artist'].lower().replace(" ","-")+"\\"+body['track'].lower().replace(" ","-")

        library.tb.create_recursive_diretory(path)

        library.json.export_json(path+"\\"+body['track_id']+".json",{
            "Artist":body['artist'],
            "Track":body["track"],
        })

        db.append({
            "Artist":body['artist'],
            "Track":body["track"],
            "src":"/"+body['artist'].lower().replace(" ","-")+"/"+body['track'].lower().replace(" ","-")
        })

library.json.export_json(app.track_database(),db)


