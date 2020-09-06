from mido import MidiFile
import library.tb
import library.json
import library.midi
import json

   
def midi_output(mid):

    array=[]
    
    for i, track in enumerate(mid.tracks):

        for msg in track:

            msg = str(msg)

            msg = msg.split(" ")

            for tag in msg:

                if "channel" in tag:
                    channel = tag.replace("channel=","")
                        

                if "note" in tag and "note_on" not in tag and "note_off" not in tag and "notes" not in tag:
                    note_value = tag.replace("note=","")
                    array.append(note_value)
                           
    return array

######

tb = library.tb

setup = library.json.import_json("setup.json")

for track_details in library.json.import_json(setup["track_database"]):

    midi_filename = setup["midi_library_location"]+track_details["track_id"]+".mid"

    try:
        library.json.import_json(setup["api_path"]+track_details["path"]+".json")["midi"]
        pass
    except KeyError:
        try:
            mid = MidiFile(setup["midi_library_location"]+track_details["track_id"]+".mid")
            pass
        except EOFError as error:
            print("Error on import " + track_details["path"])
            pass
        except OSError as error:
            print("Error on import " + track_details["path"])
            pass
        else:

            channel_number=[]
            note_list=[]

    

            scale_notes = {}
            for target_list in library.tb.removeDuplicates(midi_output(mid)):

                
                scale_notes[target_list] = midi_output(mid).count(target_list)


            pass


            library.json.update_json(setup["api_path"]+track_details["path"]+".json",{
                "note_sequence":note_list,
                "note_used":scale_notes
            })

            tb.returnMessage("Adding" + track_details["path"])
    else:
        pass
        tb.returnMessage("Already Added" + track_details["path"])


       
     
