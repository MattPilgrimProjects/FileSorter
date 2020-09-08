from app import setup
from library.scan import scan_file_recursively

from library.json import import_json
from library.json import update_json

raw_content = setup["midi_library_location"]+"processed\\*.json"

test = scan_file_recursively(raw_content)

print(test)






    # try:
    #     import_json(setup["api_path"]+track_details["path"]+".json")
    #     pass
    # except KeyError:
    #     try:
    #         mid = MidiFile(midi_filename)
    #         pass
    #     except EOFError as error:
    #         print("Error on import " + track_details["path"])
    #         pass
    #     except OSError as error:
    #         print("Error on import " + track_details["path"])
    #         pass
    #     else:

            

    #         channel_number=[]
    #         note_list=[]

            

    #         scale_notes = {}
    #         for target_list in library.tb.removeDuplicates(midi_output(mid)):

                
    #             scale_notes[target_list] = midi_output(mid).count(target_list)


    #         pass


    #         update_json(setup["api_path"]+track_details["path"]+".json",{
    #             "note_sequence":note_list,
    #             "note_used":scale_notes
    #         })

    #         tb.returnMessage("Adding to API" + track_details["path"])

    # else:
    #     pass
        
    #     tb.returnMessage("Already Uploaded to API: " + track_details["path"])

