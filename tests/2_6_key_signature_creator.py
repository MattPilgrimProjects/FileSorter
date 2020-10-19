import app
import library

app.comment.returnMessage("Starting")   

midi = app.json.import_json("midi.json")

for setting in app.settings['stage']:

    
    for filename in app.scan.scan_file_recursively(setting["midi_body_structure"]+"*.json"):

        keyword = app.parser.find_and_replace_array(filename,{
           setting["midi_body_structure"]:"",
            ".json":""
        })



        body = app.json.import_json(filename)

        array={}

        for schema in body:

            if "channel" in schema:

                main=[]

                for midi_key,count in body[schema].items():
                    main.append(midi[midi_key])
                
                array[schema]=main

        library.comment.returnMessage(setting["raw_key_signatures"]+keyword+".json")
            
        library.json.export_json(setting["raw_key_signatures"]+keyword+".json",array)
      