import app
import library.comment
import library.scan
import library.file
import library.csv
    
instrument_type_array = library.json.import_json("S:\\Midi-Library\\instruments_types.json")

main_array=[]

csv_data=[]

library.comment.returnMessage("Starting")   

for setting in app.settings['stage']:

    
    for filename in library.scan.scan_file_recursively("S:\\Midi-Library\\raw_midi\\freemidi\\processed\\json\\*.json"):

        keyword = library.parser.find_and_replace_array(filename,{
            "S:\\Midi-Library\\raw_midi\\freemidi\\processed\\json\\":"",
                ".json":""
            })

        if library.file.file_exists(filename) and library.file.file_does_not_exists(setting["midi_body_structure"]+keyword+".json"):
          
            if library.json.import_json(filename) ==None:
                library.comment.returnMessage("Error on "+ filename)
            else:
                array=[]
                note_array=[]
                channel_array=[]          

                library.comment.returnMessage("Proccessing: "+filename)   
                
                minimize_array={}

                num=0

                for channel in library.json.import_json(filename): 

                    num = num+1

                    channel_return="-"
                    

                    # for midi_array in ["BASS","Bass","bass","Acoustic Bass","Electric Bass (finger)","Electric Bass (pick)","Fretless Bass","Slap Bass 1","Slap Bass 2","Synth Bass","Synth Bass 2"]:
                  
                    #     if midi_array in channel['channel']:
                    #         channel_return = "Bass"
                    #     else:
                    #         pass
                    
                    
                    category_match=instrument_type_array[channel['instrument']]

                             
                    csv_data.append({
                        "old_channel":channel['channel'],
                        "possible_match":channel['instrument'],
                        "category_match":category_match,
                        "check_data":setting["import_midi"]["download_location"]+keyword+".mid",
                        "check_json_data":filename
                    })

                        
                    if channel["body"]:
                        minimize_array[str(num)+": "+category_match]=library.parser.distinct(channel["body"])
                    else:
                        pass

            array.append(minimize_array)
                    
            library.json.export_json(setting["midi_body_structure"]+keyword+".json",array[0])   
            library.comment.returnMessage(setting["midi_body_structure"]+keyword+".json                                ")   
        else:
            pass
  
library.csv.export_csv("S:\\Midi-Library\\draft_channel_check.csv",["old_channel","possible_match","category_match","check_data","check_json_data"],csv_data)
library.comment.returnMessage("Completed")


