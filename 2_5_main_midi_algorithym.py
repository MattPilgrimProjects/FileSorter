import app
import library.json
import library.scan
import library.file
import library.comment

import numpy

def destinct(array,channel):

    return_array=[]

    for key in array:

        if key[1] == channel and key[0] =="note_on":
            return_array.append(key[2].replace("note=",""))
        else:
            pass

        pass

    
    a = numpy.array(return_array)
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

        note_array=[]
        channel_array=[]

        
        keyword = app.parser.find_and_replace_array(filename,{
           setting["raw_midi_to_json"]:"",
            ".json":""
        })

        app.comment.returnMessage("Proccessing: "+keyword+".json") 

        for channel in library.json.import_json(filename):

            note_array.append(channel)
            channel_array.append(channel[1])
                
            channel_array = list(dict.fromkeys(channel_array))

            array={}

            for channel in channel_array:

                array[channel]=destinct(note_array,channel)

        app.json.export_json(setting["midi_body_structure"]+keyword+".json",array)   
        app.comment.returnMessage(setting["midi_body_structure"]+keyword+".json")   
  