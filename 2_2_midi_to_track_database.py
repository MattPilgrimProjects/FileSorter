import app
import config
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

        if high >= 50.0:
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

#### This is a very slow process so ensure to run when PC is not being used ####

# library.comment.returnMessage("Start")
# for source in app.settings["sources"]:
#     input_database = "S:\\Midi-Library\\"+source+"\\midi-library.json"
#     output_database = "S:\\Midi-Library\\"+source+"\\midi-library\\check.json"
#     library.comment.returnMessage("Collating missing data from "+source)
#     midi_to_track_database(input_database,output_database)
# library.comment.returnMessage("Completed")

##################################################################################

track_database = app.settings["track_database"]

export_dictionary = []


def midi_library_by_source(database, source, artist, track):

    export_dictionary_list = []
    i=0
    for schema in database:

        for final_match in schema["smart_match"]["final_match"]:

            if artist == final_match["artist"] and track == final_match["track"]:

                i=i+1

                if i==1:
                    filename = final_match["filename"]+".mid"
                else:
                    filename = final_match["filename"]+"-"+str(i)+".mid"

                export_dictionary_list.append({
                    "import": schema["midipath"],
                    "export": "S:\\Midi-Library\\"+source+"\\midi\\"+filename
                })

            else:
                pass
  
    return library.parser.remove_duplicates_from_dictionary(export_dictionary_list)

def return_information(lst,schema,key):
    export_list=[]
    for data in lst:

        if schema["artist"] == data["artist"] and schema["track"] == data["track"]:


            export_list.append(data[key])

    return export_list

def create_full_listings():

    export_dictionary = []


    for data in library.json.import_json(track_database):

        data["sources"] = {
            "mididb": midi_library_by_source(config.database["mididb"], "mididb", data["artist"], data["track"]),
            "freemidi": midi_library_by_source(config.database["freemidi"], "freemidi", data["artist"], data["track"]),
            "midiworld": midi_library_by_source(config.database["midiworld"], "midiworld", data["artist"], data["track"])
        }

        data["key_signature"] = return_information(config.database["musicnotes"],data,"midipath")

        export_dictionary.append(data)

    return library.json.export_json("S:\\Midi-Library\\midi_library.json", export_dictionary)

create_full_listings()