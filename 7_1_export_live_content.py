import app
import library.json
import library.scan
import library.directory
import library.file
import library.cron
import library.csv

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
            "sources":[
                {
                    "title":"Spotify",
                    "img":"https://www.scdn.co/i/_global/touch-icon-114.png",
                    "href":library.json.import_json(content["api_sources"]["spotify"]["track_list"])
                },
                {
                    "title":"YouTube",
                    "img":"https://www.youtube.com/s/desktop/db70be64/img/favicon_144.png",
                    "href":library.json.import_json(content["api_sources"]["youtube"]["track_list"])
                },
                {
                    "title":"Apple Music",
                    "img":"https://music.apple.com/assets/favicon/favicon-180-c132a95549a91ae6983a4914da3e1c44.png",
                    "href":library.json.import_json(content["api_sources"]["apple"]["track_list"])
                }
            ],
            "album_list":library.json.import_json(content["api_sources"]["spotify"]["album_list"]),
            "adverts":content["api_sources"]["karaoke_version"]["affiliate_link"]
        })

### Create Directories
www_export=[]

for content in library.json.import_json("Z:\\full_list.json"):
    library.directory.create_recursive_directory("S:/Website Projects/api"+content["url"])


library.cron.delay(1)

amazon=[]

library.comment.returnMessage("Start")

for content in library.json.import_json("Z:\\full_list.json"):

    if content["sources"]["freemidi"]["json"] and content["parsed"]["freemidi"]["compile_midi_file"] and content["parsed"]["freemidi"]["key_signature_created"]:
        export_profile(content)
    else:
        pass
    
    if content["api_sources"]["spotify"]["album_list"] and content["api_sources"]["spotify"]["track_list"] and content["api_sources"]["youtube"]["track_list"] and content["api_sources"]["apple"]["track_list"]:
        export_sidebar(content)
    else:
        pass

    if library.file.file_exists("S:/Website Projects/api"+content["url"]+"/profile.json") and library.file.file_exists("S:/Website Projects/api"+content["url"]+"/sidebar.json"):

        www_export.append({
                "artist":content["artist"],
                "track":content["track"],
                "url":content["url"]
        })
    else:
        library.directory.remove_directory("S:/Website Projects/api"+content["url"])
        


# # library.csv.export_csv("Z:\\apple_music\\raw_data\\apple.csv",["artist","track","url"],www_export)
library.json.export_json("S:/Website Projects/api/www.json",www_export)

library.comment.returnMessage("Complete")