import app
import config
import library.download

track_database = app.settings["track_database"]
export_filename = "S:\\Midi-Library\\url\\midi_library.json"

def create_midi_files_dictionary():

    export_list = []

    for data in library.json.import_json(track_database):

        export_list.append(config.source_return(data))

    return library.json.export_json(export_filename,export_list)

create_midi_files_dictionary()
library.download.download_midi(export_filename)
