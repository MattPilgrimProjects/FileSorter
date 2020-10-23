import app
import library.json
import library.scan
import library.file
import library.comment

import numpy

def destinct(array):
   
    a = numpy.array(array)
    unique, counts = numpy.unique(a, return_counts=True) 

    test =  dict(zip(unique, counts))

    return_array_2={}

    for key,value in test.items():

        return_array_2[key]=str(value)

    return return_array_2

###########################################################################

main_array=[]

app.comment.returnMessage("Starting")   

for setting in app.settings['stage']:

    
    for filename in app.scan.scan_file_recursively(setting["raw_midi_to_json"]+"*.json"):

        keyword = app.parser.find_and_replace_array(filename,{
            setting["raw_midi_to_json"]:"",
                ".json":""
            })

        if library.file.file_exists(filename):
          
            if library.json.import_json(filename) ==None:
                library.comment.returnMessage("Error on "+ filename)
            else:
                array=[]
                note_array=[]
                channel_array=[]          

                app.comment.returnMessage("Proccessing: "+filename)   
                
                minimize_array={}

                for channel in library.json.import_json(filename):                   

                    minimize_array[channel['channel']]=destinct(channel["body"])

            array.append(minimize_array)
                    
        app.json.export_json(setting["midi_body_structure"]+keyword+".json",array[0])   
        app.comment.returnMessage(setting["midi_body_structure"]+keyword+".json")   
  