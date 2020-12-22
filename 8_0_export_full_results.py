import app
import library.scan
import library.json
import library.file
import library.comment
import library.url
import library.directory
import sys

track_database = app.settings["main_database_file"]
live_database = "S:\\Website Projects\\MusicKeyFinder\\resources\\api\\"
key_signature = "S:\\Midi-Library\\key_signature\\"
amazon_album_list  =app.settings["amazon"]["output"]
spotify_track_list = app.settings["spotify"]["track_list"]
youtube_track_list = app.settings["youtube"]["track_list"]
apple_music_track_list = app.settings["apple_music"]["track_list"]

original_track_list = app.settings["karaokeversion"]["compressed"]


for data in library.json.import_json(original_track_list):

    filename = data["filename_artist"]+"-"+data["filename_track"]

    profile = live_database+data["filename_artist"]+"\\"+data["filename_track"]+"\\profile.json"
    sidebar = live_database+data["filename_artist"]+"\\"+data["filename_track"]+"\\sidebar.json"
    spotify_source = spotify_track_list+filename+".json"
    youtube_source = youtube_track_list+filename+".json"
    amazon_source = amazon_album_list+filename+".json"
    apple_music_source = apple_music_track_list+filename+".json"

    if library.file.file_exists(key_signature+filename+".json") and library.file.file_exists("S:\\Midi-Library\\parsed\\matched\\processed\\"+filename+".json"):
        library.directory.create_recursive_directory(live_database+data["url"])
        # library.comment.returnMessage("Adding Profile "+data["filename"])

        last_fm = library.json.import_json("S:\\Midi-Library\\parsed\\matched\\processed\\"+filename+".json")
        content = library.json.import_json(key_signature+filename+".json")

        library.json.export_json(profile,{
            "artist":data["artist"],
            "track":data["track"],
            "profile":last_fm[0]["last_fm"],
            "content":content["results"]
        })
        
    if library.file.file_exists(amazon_source) and library.file.file_exists(youtube_source) and library.file.file_exists(spotify_source):

        library.directory.create_recursive_directory(live_database+data["url"])

        # library.comment.returnMessage("Adding Sidebar "+data["filename"])

        apple = library.json.import_json("S:\\Midi-Library\\apple_music\\track_list\\"+filename+".json")

        library.json.export_json(sidebar,{
            "sources":{
                "Spotify":library.json.import_json(spotify_source),
                "YouTube":library.json.import_json(youtube_source),
                "Apple Music":apple
            },
            "album_list":library.json.import_json(amazon_source),
            "adverts":"https://www.karaoke-version.com/afflink.html?aff=948&action=redirect&part=custom&song="+data["track"]+"&artist="+data["artist"]
        })

array=[]

for data in library.json.import_json(track_database):

    profile = live_database+data["filename_artist"]+"\\"+data["filename_track"]+"\\profile.json"
    sidebar = live_database+data["filename_artist"]+"\\"+data["filename_track"]+"\\sidebar.json"

    if library.file.file_exists(profile) and library.file.file_exists(sidebar):
        array.append({
            "artist":data["artist"],
            "track":data["track"],
            "url":data["url"]
        })

library.json.export_json(live_database+"www.json",array)
library.comment.returnMessage("Completed")
# sys.exit()


# library.file.file_update("S:\\Desktop\\results.txt",[ 
#     "##################################################",
#     "Start Time: "+start
   
# ])


