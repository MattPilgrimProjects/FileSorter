import app
import library.json
import library.scan
import library.directory
import library.file
import library.cron

def export_profile(content):

    audio_data=[]
    for content_1 in content["parsed"]["freemidi"]["compile_midi_file"]:
        audio_data.append(library.json.import_json(content_1))

    key_signature=[]
    for content_2 in content["parsed"]["freemidi"]["key_signature_created"]:
        key_signature.append(library.json.import_json(content_2))
        


    return library.json.export_json(
        "S:/Website Projects/api"+content["url"]+"/profile.json",
        {
            "artist":content["artist"],
            "track":content["track"],
            "audio_data":audio_data,
            "key_signatures":key_signature
        })
    
def export_sidebar(content):
    return library.json.export_json(
        "S:/Website Projects/api"+content["url"]+"/sidebar.json",
        {
            "playback":{
                "spotify":library.json.import_json(content["api_sources"]["spotify"]["track_list"]),
                "youtube":library.json.import_json(content["api_sources"]["youtube"]["track_list"]),
                "album_list":library.json.import_json(content["api_sources"]["spotify"]["album_list"])
            },
            "adverts":content["api_sources"]["karaoke_version"]["affiliate_link"]
        })

### Create Directories
www_export=[]

for content in library.json.import_json("full_list.json"):

    if  content["sources"]["freemidi"]["midi"] and content["sources"]["freemidi"]["json"] and content["parsed"]["freemidi"]["compile_midi_file"] and content["parsed"]["freemidi"]["key_signature_created"] and content["api_sources"]["spotify"]["album_list"] and content["api_sources"]["spotify"]["track_list"] and content["api_sources"]["youtube"]["track_list"]:

        library.directory.create_recursive_directory("S:/Website Projects/api"+content["url"])

        www_export.append({
            "artist":content["artist"],
            "track":content["track"],
            "url":content["url"]
        })





for content in library.json.import_json("full_list.json"):

    if content["sources"]["freemidi"]["midi"] and content["sources"]["freemidi"]["json"] and content["parsed"]["freemidi"]["compile_midi_file"] and content["parsed"]["freemidi"]["key_signature_created"] and library.file.file_exists("S:/Website Projects/api"+content["url"]):

        export_profile(content)
    
    if content["api_sources"]["spotify"]["album_list"] and content["api_sources"]["spotify"]["track_list"] and content["api_sources"]["youtube"]["track_list"] and library.file.file_exists("S:/Website Projects/api"+content["url"]):
        export_sidebar(content)

library.json.export_json("S:/Website Projects/api/www.json",www_export)



# profile=[
#     artist,
#     track,
#     audio_data,
#     key_signature
# ]

# sidebar=[
#     playback
#     spotify->href
#     youtube->href
#     apple_music->href
#     album_list
# ]