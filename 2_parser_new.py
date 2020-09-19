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


    print(str(data).title())


    track = data.split(">",1)[1].replace(" ","-").lower()

    fixed_track = track.replace("-"," ").title()

 
    data = data.replace(track,fixed_track)


    data = data.replace("--","")



    return data

for filename in filelist:

    for data in library.tb.importCSVData(filename):
        
        if data[0]=="href":
            pass
        else:   
  
            data = config_handler(data) 
         
            group = data.split("-")
            

            if check_key_array(group,app.app_setup(1)['config']['track_id']) is not None:

                track_id = re.findall(r'\d+', check_key_array(group,app.app_setup(1)['config']['track_id']) )

                if check_key_array(track_id,0) is not None:

                    return_data={
                            "track_id": check_key_array(track_id,0),
                            "artist": check_key_array(group,app.app_setup(1)['config']['artist']),
                            "track": check_key_array(group,app.app_setup(1)['config']['track'])
                    }

                    array.append(return_data)
        
library.json.export_json(app.app_setup(2)["export"]["track_listing"],array)

 



