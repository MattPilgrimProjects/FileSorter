import app
import library.tb
import library.json
import re

filelist = library.tb.returnAllFilesByExtension(app.app_setup(1)['storage']['local_path_csv_processed'],".csv")

array=[]

def check_key_array(array,key):
    try:
        array[key]
    except IndexError:
        pass
    else:
        return array[key].strip()    

def config_handler(data):

    data = data[0]

    data = data.split(app.app_setup(1)['config']['start'],1)[1]

    data = data.split(app.app_setup(1)['config']['end'], 1)[0]
    
    key_attributes=app.app_setup(1)['config']['replace_array']

    for key,value in key_attributes.items():

        data = data.replace(key,value)

        pass    

    function_title =app.app_setup(1)['config']['title']


    return preset_handler(function_title,data)
   

def preset_handler(function_title,data):
    
    if function_title =="1":

        data = str(data).title()

        track_id = data.split("-")[0]

        data = data.replace(track_id+"-","")

        track_with_dashes = data.split(">")[1].replace(" ","-")

        remove_id = data.replace(track_id,"")

        artist = remove_id.replace(track_with_dashes+"-","").split(" ")[0].replace("-"," ")

        track = track_with_dashes.replace("-"," ")
    
    else:
        pass

    if function_title =="2":

        track = check_key_array(data.split("-"),0)
        artist = check_key_array(data.split("-"),1)
        track_id = check_key_array(data.split("-"),2)
        track_id = check_key_array(sanitize("track_id",track_id),0)
        artist = str(artist)
        artist = artist.replace("_"," ")

    return [
        track_id,
        artist,
        track
    ]


def sanitize(title,variable):
    return re.findall(app.regex_filter()[title], str(variable) )
    

 
for filename in filelist:

    for data in library.tb.importCSVData(filename):
        
        if data[0]=="href":
            pass
        else:   
  
            group = config_handler(data) 

            if group[0] is not None:

                array.append({
                    "track_id": group[0],
                    "artist": group[1],
                    "track": group[2]
                })
            else:
                pass
        
library.json.export_json(app.app_setup(2)["export"]["track_listing"],array)
