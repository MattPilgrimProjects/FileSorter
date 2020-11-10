import app
import library.scan
import library.json
import library.file
import library.comment
import library.url

track_profiles = library.scan.import_json_from_directory_recursively("S:\\Midi-Library\\tracks\\freemidi\\*\\*\\*.json")

artist_profiles = library.scan.import_json_from_directory_recursively("S:\\Midi-Library\\artist\\freemidi\\processed\\*.json")

output=[]

def freemidi_json(original_list,file_extension):

    artist=[]

    for test in artist_profiles:

        if test["artist"] == original_list["artist"]:
            artist.append(test['raw_artist'])
        else:
            pass 

    hyperlink=[]

    for profile in track_profiles:
        
        if original_list["track"] == profile["track"] and profile["raw_artist"] in artist:
            
            filename = profile["url"].replace("https://freemidi.org/","S:\\Midi-Library\\raw_midi\\freemidi\\processed\\json\\").replace("\\","/")+".json"

            if library.file.file_exists(filename):
                hyperlink.append(filename)
            else:
                pass

        else:
            pass

    return hyperlink

def freemidi_key_signature_filename(profile):
    return profile["url"].replace("https://freemidi.org/","S:\\Midi-Library\\raw_key_signatures\\freemidi\\").replace("\\","/")+".json"

def freemidi_compile_midi_filename(profile):
    return profile["url"].replace("https://freemidi.org/","S:\\Midi-Library\\raw_midi_body_structure\\freemidi\\").replace("\\","/")+".json"

def freemidi_json_filename(profile):
    return profile["url"].replace("https://freemidi.org/","S:\\Midi-Library\\raw_midi\\freemidi\\processed\\json\\").replace("\\","/")+".json"

def freemidi_midi_filename(profile):
    return profile["url"].replace("https://freemidi.org/","S:\\Midi-Library\\raw_midi\\freemidi\\processed\\").replace("\\","/")+".mid"

def freemidi(original_list,file_extension):

    artist=[]

    for test in artist_profiles:

        if test["artist"] == original_list["artist"]:
            artist.append(test['raw_artist'])
        else:
            pass 

    hyperlink=[]

    for profile in track_profiles:

        if original_list["track"] == profile["track"] and profile["raw_artist"] in artist:

            if file_extension=="midi": filename = freemidi_midi_filename(profile)
            if file_extension=="json": filename = freemidi_json_filename(profile)
            if file_extension=="compile_midi_file": filename = freemidi_compile_midi_filename(profile)
            if file_extension=="key_signature_created": filename = freemidi_key_signature_filename(profile)
 
            if library.file.file_exists(filename):
                hyperlink.append(filename)
            else:
                pass

        else:
            pass

    return hyperlink

def api_file_check(directory,url):

    filename = url[1:].replace("/","-")+".json"

    filepath = directory.replace("\\","/")+filename

    if library.file.file_exists(filepath):
        return filepath
    else:
        return ""


########################################################################################################################

# Filepath Setup

spotify_raw_data = "S:\\Midi-Library\\spotify\\raw_data\\"
spotify_album_list = "S:\\Midi-Library\\spotify\\album_list\\"
spotify_track_list = "S:\\Midi-Library\\spotify\\track_list\\"

youtube_raw_data="S:\\Midi-Library\\youtube\\raw_data\\"
youtube_track_list="S:\\Midi-Library\\youtube\\track_list\\"

########################################################################################################################


start = library.comment.returnMessage("Start")

for original_list in library.scan.import_json_from_directory_recursively(app.settings["sources"]["track_list"]["json"]):      

    output.append({   
        "artist":original_list["artist"],
        "track":original_list["track"],
        "url":original_list["url"],
        "sources":{
            "freemidi":{
                "midi":freemidi(original_list,"midi"),
                "json":freemidi(original_list,"json")
            }
        },
        "parsed":{
            "freemidi":{
                "compile_midi_file":freemidi(original_list,"compile_midi_file"),
                "key_signature_created":freemidi(original_list,"key_signature_created")
            }
        },
        "api_sources":{
            "spotify":{
                "raw_data":api_file_check(spotify_raw_data,original_list["url"]),
                "album_list":api_file_check(spotify_album_list,original_list["url"]),
                "track_list":api_file_check(spotify_track_list,original_list["url"])
            },
            "youtube":{
                "raw_data":api_file_check(youtube_raw_data,original_list["url"]),
                "track_list":api_file_check(youtube_track_list,original_list["url"])
            },
            "karaoke_version":{
                "affiliate_link":"https://www.karaoke-version.com/afflink.html?aff=948&action=redirect&part=custom&song="+original_list["track"]+"&artist="+original_list["artist"]
            }
        }
    })

library.json.export_json("full_list.json",output)
end = library.comment.returnMessage("Completed")

###################################################################################################################################################################################

score_sources_freemidi_midi=0

score_sources_freemidi_json=0

score_parsed_freemidi_compile_midi_file=0

score_parsed_freemidi_key_signature_created=0

score_api_sources_spotify_raw_data=0

score_api_sources_spotify_album_list=0

score_api_sources_spotify_track_list=0

score_api_sources_youtube_raw_data=0

score_api_sources_youtube_track_list=0

total=0

for items in library.json.import_json("full_list.json"):

    total=total+1

    freemidi_sources = items["sources"]["freemidi"]

    freemidi_parsed = items["parsed"]["freemidi"]

    
    if freemidi_sources["midi"]: score_sources_freemidi_midi=score_sources_freemidi_midi+1
    
    if freemidi_sources["json"]: score_sources_freemidi_json=score_sources_freemidi_json+1

    if freemidi_parsed["compile_midi_file"]: score_parsed_freemidi_compile_midi_file=score_parsed_freemidi_compile_midi_file+1
    
    if freemidi_parsed["key_signature_created"]: score_parsed_freemidi_key_signature_created=score_parsed_freemidi_key_signature_created+1


    spotify =items["api_sources"]["spotify"] 

    if spotify["raw_data"]: score_api_sources_spotify_raw_data=score_api_sources_spotify_raw_data+1

    if spotify["album_list"]: score_api_sources_spotify_album_list=score_api_sources_spotify_album_list+1

    if spotify["track_list"]: score_api_sources_spotify_track_list=score_api_sources_spotify_track_list+1

    youtube = items["api_sources"]["youtube"]

    if youtube["raw_data"]: score_api_sources_youtube_raw_data=score_api_sources_youtube_raw_data+1

    if youtube["track_list"]: score_api_sources_youtube_track_list=score_api_sources_youtube_track_list+1


library.file.file_update("S:\\Desktop\\results.txt",{
    "",
    "##################################################",
    "Start Time: "+start,
    "End Time: "+end,
    "---",
    "Sources from Freemidi midi: "+str(score_sources_freemidi_midi)+"/"+str(total),
    "Sources from Freemidi json: "+str(score_sources_freemidi_json)+"/"+str(total),
    "---",
    "Parsed Freemidi content: "+str(score_parsed_freemidi_compile_midi_file)+"/"+str(total),
    "Parsed Freemidi key signature: "+str(score_parsed_freemidi_key_signature_created)+"/"+str(total),    
    "---",
    "Spotify raw data: "+str(score_api_sources_spotify_raw_data)+"/"+str(total),
    "Spotify album list: "+str(score_api_sources_spotify_album_list)+"/"+str(total),
    "Spotify track list: "+str(score_api_sources_spotify_track_list)+"/"+str(total),
    "---",
    "Youtube raw data: "+str(score_api_sources_youtube_raw_data)+"/"+str(total),
    "Youtube track list: "+str(score_api_sources_youtube_track_list)+"/"+str(total),
    ""
})


