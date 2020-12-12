import app
import library.json
import library.comment
import library.file
import sys

track_database = app.settings["track_database"]


def return_artist_list(value):
    artist_list = []
    for schema in library.json.import_json(track_database):
        artist_list.append(schema[value])
    return library.parser.remove_duplicates_from_array(artist_list)

def artist_smart_match(artist_list, data):

    artist_match_list = []

    for check_artist in artist_list:

        high = library.parser.high_match_percentage(check_artist, data)

        if high >= 80.0:
            artist_match_list.append((check_artist, high))

    return library.parser.convert_tuples_to_dictionary(artist_match_list)

def smart_match_final(artist_list,track_list):

    return_list=[]

    for schema in library.json.import_json(track_database):

        if schema["artist"] in artist_list and schema["track"] in track_list:
            return_list.append(schema)

    return return_list

def smart_match(data, artist_list, track_list):

    artist_match = artist_smart_match(artist_list, data["artist"])
    track_match = artist_smart_match(track_list, data["track"])

    final_artist_match = []
    for artist in artist_match: final_artist_match.append(artist)

    final_track_match=[]
    for track in track_match: final_track_match.append(track)
        
   
    return {
        "artist_match": artist_match,
        "track_match": track_match,
        "final_match": smart_match_final(final_artist_match,final_track_match)
    }

def midi_to_track_database(input_database,output_database):
    
    export_bad_library = []

    artist_list = return_artist_list("artist")
    track_list = return_artist_list("track")

    for data in library.json.import_json(input_database):

        library.comment.returnMessage("Processing:"+data["artist"]+" - "+data["track"])

        export_bad_library.append({
                "artist": data["artist"],
                "track": data["track"],
                "midipath": data["midipath"],
                "smart_match": smart_match(data, artist_list, track_list)
        })

        library.comment.returnMessage("Completed: "+data["artist"]+" - "+data["track"])
        library.comment.returnMessage("---")

    return library.json.export_json(output_database, export_bad_library)

library.comment.returnMessage("Start")
source="mididb"
input_database = "S:\\Midi-Library\\"+source+"\\midi-library.json"
output_database = "S:\\Midi-Library\\"+source+"\\midi-library\\check.json"


export_list=[]
export_midi_list=[]
for data in library.json.import_json("S:\\Midi-Library\\"+source+"\\midi-library\\perfect.json"):
    if library.file.file_exists(data["export"]):
        pass
    else:
        export_midi_list.append(data["import"])


export_list_1=[]
for schema in library.json.import_json("S:\\Midi-Library\\"+source+"\\midi-library.json"):
    
    export_list_1.append(schema)
    

library.json.export_json("S:\\Midi-Library\\"+source+"\\midi-library_1.json",export_list_1)


library.comment.returnMessage("Collating missing data from "+source)
# for source in app.settings["sources"]:
midi_to_track_database(input_database,output_database)


# export_json_content=[]
# midi_library_remove=[]
# for data in library.json.import_json(output_database):

#     for schema in data["smart_match"]["final_match"]:

#         midi_library_remove.append(data["midipath"])

#         export_json_content.append({
#             "artist":schema["artist"],
#             "track":schema["track"],
#             "import":data["midipath"],
#             "export":"S:\\Midi-Library\\mididb\\midi\\"+schema["filename"]+".mid"
#         })

# new_midi_library=[]
# for data in library.json.import_json(input_database):

#     if data["midipath"] in midi_library_remove:
#         pass
#     else:
#         new_midi_library.append(data)
 

# library.json.export_json(input_database,new_midi_library)
# library.json.export_json("S:\\Midi-Library\\"+source+"\\midi-library\\perfect.json",export_json_content)
# library.comment.returnMessage("Completed")
