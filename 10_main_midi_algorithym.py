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

    test = dict(zip(unique, counts))

    return str(test)



###########################################################################

for schema in app.json.import_json(app.settings["live_database"]):

    if app.file.file_exists(app.settings["raw_midi_to_json"]+schema["title"]+"\\"+schema["track_id"]+".json"):
        app.directory.create_recursive_diretory(app.settings["live_api"]+schema["url"])
        print(app.settings["live_api"]+schema["url"]+"/"+schema["track_id"]+".json")
        
        pass
    else:
        pass

  

 
    pass


# for schema in app.settings["stage"]:

   
#     for filename_2 in library.scan.scan_file_recursively(app.settings["live_api"]+"**\\*.json"):

#         url = filename_2.replace(app.settings["live_api"],"")

#         artist = url.split("\\")[0]

#         track = url.split("\\")[1]

#         track_id = url.split("\\")[2].replace(".json","")

        
#         if library.file.file_exists(schema["raw_midi_to_json"]+track_id+".json"):
#             channel_array=[]
#             note_array=[]

#             for channel in library.json.import_json(schema["raw_midi_to_json"]+track_id+".json"):

#                 note_array.append(channel)
#                 channel_array.append(channel[1])
            
#             channel_array = list(dict.fromkeys(channel_array))

#             array={}

#             array["midi_body_structure"]={}

#             for channel in channel_array:

#                 array["midi_body_structure"][channel]=destinct(note_array,channel)
            
#             library.json.update_json(filename_2,array)
#             library.comment.returnMessage("Completed =>"+filename_2)
   



















