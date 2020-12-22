
# def learning(single,array):
#     return_array=[]
#     for value in array:

#         if single in value or single.title() in value:
#             return_array.extend({
#                 value
#             })

#     return return_array

# def artist_match(single,array):
#     return_array=[]
#     for value in array:

#         est = library.parser.high_match_percentage(single,value)
        
#         if  est >= 25:

#             return_array.append({
#                 value:est,
#             })
#     return return_array
    
# def clever_match_artist_to_track(artist_array,track_array):
    
#     array=[]
#     for data in library.json.import_json(original_track_list):
#         if data["artist"] in artist_array and data["track"] in track_array:
#             array.append(data)
#     return array

# def export_learning_results():
#     return_json=[]
#     for data  in library.json.import_json("S:\\Midi-Library\\parsed\\compressed.json"):


#         match_to_artist = learning(data["artist"],artist_list)
#         match_to_track = learning(data["track"],track_list)
#         match_artist_to_track = clever_match_artist_to_track(match_to_artist,match_to_track)
            
#         return_json.append({
#                 "artist":data["artist"],
#                 "track":data["track"],
#                 "tags":data["tags"],
#                 "clever_match_artist":match_to_artist,
#                 "clever_match_track":match_to_track,
#                 "clever_match_artist_to_track":match_artist_to_track
#         })
#         library.comment.returnMessage("Processing: "+data["artist"]+" "+data["track"])

#     return library.json.export_json("S:\\Midi-Library\\sources\\learning.json",return_json)

# def compile_list():
#     array = []

#     for data in library.scan.import_json_from_directory_recursively_items(source_path+"*.json"):

#         for schema in data["data"]:

#             if schema != "track":
#                 try:
#                     schema["name"]
#                 except:
#                     pass
#                 else:

#                     if int(schema["playcount"]) >= 10000:
#                         library.comment.returnUpdateMessage("Adding: "+schema["artist"]["name"] +" - "+schema["name"])
#                         array.append({
#                             "artist": schema["artist"]["name"],
#                             "track": schema["name"],
#                             "listeners": schema["listeners"],
#                             "playcount": schema["playcount"],
#                             "tag_1":schema["tags"][0]["name"]
#                         })

#     library.csv.export_csv(
#         compressed_path, ["artist", "track", "listeners", "playcount","tag_1"], array)


# def create_compressed_list():

#     playcount_list=[]
#     for data in library.json.import_json("S:\\Midi-Library\\parsed\\uncompressed.json"):
#         playcount_list.append(int(data["playcount"]))
    
#     playcount_list.sort()

#     new_playcount=[]

#     for counts  in playcount_list:

#         if counts > 1000000:
#             new_playcount.append(counts)
    
#     compressed_dictionary=[]

#     for schema  in library.json.import_json("S:\\Midi-Library\\parsed\\uncompressed.json"):

#         if int(schema["playcount"]) in new_playcount:
#             compressed_dictionary.append(schema)
    
#     return library.json.export_json("S:\\Midi-Library\\parsed\\compressed.json",compressed_dictionary)

# def export_sorted_by_popular():
#     export=[]
#     for data in library.json.import_json("S:\\Midi-Library\\sources\\learning.json"):

#         match_array  = data["clever_match_artist_to_track"]

#         if len(match_array) ==1:
#             export.append(export_array_handler(match_array[0],data))
#         elif len(match_array)>=1:
#             for data_single in match_array:
#                 export.append(export_array_handler(data_single,data))
#         else:
#             pass
#     library.json.export_json(track_database,export)
#     library.comment.returnMessage("Completed: " + track_database)