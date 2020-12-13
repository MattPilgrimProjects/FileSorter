import app
import library.download
import library.json

track_database = app.settings["track_database"]

export_dictionary=[]

def midi_library_by_source(database,source,artist,track):

    export_dictionary_list=[]
    for schema in database:

        for final_match in schema["smart_match"]["final_match"]:

            if artist==final_match["artist"] and track==final_match["track"]:

                export_dictionary_list.append({
                    "import":schema["midipath"],
                    "export":"S:\\Midi-Library\\"+source+"\\midi\\"+final_match["filename"]+".mid"
                })

            else:
                pass

    return library.parser.remove_duplicates_from_dictionary(export_dictionary_list)

export_dictionary=[]

database={
    "mididb":library.json.import_json("S:\\Midi-Library\\mididb\\midi-library\\check.json"),
    "freemidi":library.json.import_json("S:\\Midi-Library\\freemidi\\midi-library\\check.json"),
    "midiworld":library.json.import_json("S:\\Midi-Library\\midiworld\\midi-library\\check.json")

}



for data in library.json.import_json(track_database):

    data["sources"]={
        "mididb":midi_library_by_source(database["mididb"],"mididb",data["artist"],data["track"]),
        "freemidi":midi_library_by_source(database["freemidi"],"freemidi",data["artist"],data["track"]),
        "midiworld":midi_library_by_source(database["midiworld"],"midiworld",data["artist"],data["track"])
    }

    export_dictionary.append(data)


library.json.export_json("S:\\Midi-Library\\midi_library.json",export_dictionary)
# library.download.download_midi(
#     "S:\\Midi-Library\\mididb\\midi-library\\perfect.json"
# )
