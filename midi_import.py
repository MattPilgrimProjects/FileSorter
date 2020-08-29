from mido import MidiFile
import library.tb
import library.json
import json

tb = library.tb

setup = library.json.import_json("setup.json")

for track_details in library.json.import_json(setup["track_database"]):

    try:
        library.json.import_json(setup["dev_path"]+track_details["path"]+".json")["midi"]
    except KeyError:
        try:
            mid = MidiFile(setup["midi_library_location"]+track_details["track_id"]+".mid")
            pass
        except EOFError as error:
            print("Error on import " + setup["midi_library_location"]+track_details["track_id"]+".mid")
            pass
        except OSError as error:
            print("Error on import " + setup["midi_library_location"]+track_details["track_id"]+".mid")
        else:

            row={}
            test=[]
            array=[]

            channel=""
            note_value=""

            returnValue={}

            for i, track in enumerate(mid.tracks):
                
                for msg in track:

                    msg = str(msg)

                    msg = msg.split(" ")

                    for tag in msg:

                        if "channel" in tag:
                            channel = tag.replace("channel=","")
                        

                        if "note" in tag and "note_on" not in tag and "note_off" not in tag and "notes" not in tag:
                            note_value = tag.replace("note=","")

                            array.append(str(channel+":"+note_value))

            
                library.json.update_json(setup["dev_path"]+track_details["path"]+".json",{
                    "midi" : tb.removeDuplicates(array),
                    "full_array":array
                    })

                tb.returnMessage("Updated " + setup["dev_path"]+track_details["path"]+".json")
    else:
        tb.returnMessage("Already Added")


          
        
             

     
