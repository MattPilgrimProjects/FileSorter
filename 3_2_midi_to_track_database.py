import app
import library.json
import library.comment

track_database = app.settings["track_database"]

def possible_track(data):
    match_list=[]

    for schema  in library.json.import_json("S:\\Midi-Library\\parsed\\mididb.json"):

        if data["track"] == schema["track"]:
            match_list.append(schema)
    
    return match_list

def possible_artist(data):
    match_list=[]

    for schema  in library.json.import_json("S:\\Midi-Library\\parsed\\mididb.json"):

        if data["artist"] == schema["artist"]:
            match_list.append(schema["artist"])
    
    return library.parser.remove_duplicates_from_array(match_list)


def mididb(data,source):

    match_list=[]

    for schema  in library.json.import_json("S:\\Midi-Library\\"+source+"\\midi-library.json"):

        if data["artist"] == schema["artist"] and data["track"] == schema["track"]:
            match_list.append(schema["midipath"])
    
    return match_list


def midi_to_track_database(source):
    library.comment.returnMessage("Collating data from "+source)
    export_perfect_library=[]
    # export_check_library=[]

    for data in library.json.import_json(track_database):

        mididb_match = mididb(data,source)
        # possible_artist_value = possible_artist(data)
        # possible_track_value = possible_track(data)

        if len(mididb_match) !=0:

            export_perfect_library.append({
                "artist":data["artist"],
                "track":data["track"],
                "filename":data["filename"],
                "midi_filename":mididb_match[0]
            })
        
        # if len(mididb_match)==0 and len(possible_artist_value) !=0 and len(possible_track_value) !=0:

        #     export_check_library.append({
        #             "artist":data["artist"],
        #             "track":data["track"],
        #             "filename":data["filename"],
        #             "possible_artist":possible_artist_value,
        #             "possible_track":possible_track_value     
        #     })

    
    # library.json.export_json("S:\\Midi-Library\\"+source+"\\midi-library\\check.json",export_check_library)
    library.json.export_json("S:\\Midi-Library\\"+source+"\\midi-library\\perfect.json",export_perfect_library)

library.comment.returnMessage("Start")
midi_to_track_database("mididb")
midi_to_track_database("midiworld")
library.comment.returnMessage("Completed")

