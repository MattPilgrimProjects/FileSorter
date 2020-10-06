



# from app import setup
# from app import app_setup
# from mido import MidiFile
# import library.tb
# import library.json
# import library.midi
# import json
# import library.filemodels


# from library.json import import_json
# from library.tb import file_exists
# ######

# tb = library.tb


# # Parse Midi Data to JSON Files

# for track_details in import_json(setup["track_database"]):

#     midi_filename = app_setup(1)["storage"]["midi_library"]+track_details["track_id"]+".mid"

#     process_filename = app_setup(1)['processing']["json_processing_path"]+track_details["track_id"]+".json"

#     raw_filename = app_setup(1)['processing']["midi_processing_path"]

#     if file_exists(process_filename) or file_exists(process_filename):
#         pass
#     else:
#         try:
#             mid = MidiFile(midi_filename)  
#         except TypeError:
#             print("TypeError - " + track_details["track_id"])
#         except EOFError:
#             print("EOFError - " +track_details["track_id"])
#         except OSError:
#             print("OSError - " +track_details["track_id"])
#         except ValueError as error_message:
#             print(str(error_message) +" - "+ track_details["track_id"])
#         else:
#             array = library.midi.export_processed_content(mid,process_filename)
#             library.json.export_json(process_filename,array)
#             library.filemodels.move_file_content(midi_filename,raw_filename)
     

     
# import app
# import library.json
# import library.comment
# import library.directory

# search_database = app.settings["search_database"]

# search_database = library.json.import_json(search_database)

# live_database = app.settings["live_database"]

# array=[]

# def freemidi(schema):

#     track_id = schema.split("-")[0]

#     track = schema.replace(schema.split("title=")[0],"").replace("title=","")

#     track_in_lower_case = track.lower().replace(" ","-")

#     artist = schema.replace(track_in_lower_case,"").replace(track_id+"--","").split(" ")[0].title().replace("-"," ")

    

#     return{
#         "track_id":track_id,
#         "artist":artist,
#         "track":track
#         }

# def midiworld(schema):

#     track_id = schema.replace(schema.split("- ")[0]+"- ","")

#     track = schema.split("(")[0]

#     return{
#         "track_id":track_id,
#         "artist":schema.replace(") - "+track_id,"").replace(track,"").replace("(",""),
#         "track":track
#         }




# for schema in search_database:

#     if schema['title']=="freemidi":group = freemidi(schema['raw']) 

#     if schema['title']=="midiworld":group = midiworld(schema['raw'])  

#     if group["track_id"].strip().isdigit() and group["track"]!="" and group["artist"]!="":

#         track = group["track"].strip().lower().replace(" ","-")

#         for name in ["'",",",".",":","*"]:
#             track = track.replace(name,"")
#             pass

#         url = "/"+group["artist"].strip().lower().replace(" ","-")+"/"+track+"/"

#         array.append({
#             "title":schema["title"].strip(),
#             "track_id":group["track_id"].strip(),
#             "artist":group["artist"].strip(),
#             "track":group["track"].strip(),
#             "url":url
#         })

#         library.directory.create_recursive_diretory(app.settings["live_api"]+url)
   
#         library.json.export_json(app.settings["live_api"]+url+group["track_id"].strip()+".json",{
#             "Artist":group["artist"].strip(),
#             "Track":group["track"].strip()
#         })

# library.json.export_json(live_database,array)
# library.comment.returnMessage("Completed: "+live_database)