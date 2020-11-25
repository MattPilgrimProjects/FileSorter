import app
import library.json
import library.scan
import library.directory
import library.file
import library.cron
import library.csv

api_path = "S:/Website Projects/MusicKeyFinder/resources/api"

def export_profile(content): 

    freemidi_compile_midi =content["parsed"]["freemidi"]["compile_midi_file"]
    key_signature = content["parsed"]["freemidi"]["key_signature_created"]

    if key_signature and freemidi_compile_midi and content["url"]:  

        library.comment.returnMessage("Processing Profile: "+content["url"])  

        library.directory.create_recursive_directory(api_path+content["url"])

        audio_data=[]
        for content_1 in content["parsed"]["freemidi"]["compile_midi_file"]:
            audio_data.append(library.json.import_json(content_1))

        key_signature=[]
        for content_2 in content["parsed"]["freemidi"]["key_signature_created"]:
            key_signature.append(library.json.import_json(content_2))
            
        library.json.export_json(
            api_path+content["url"]+"/profile.json",
            {
                "artist":content["artist"],
                "track":content["track"],
                "audio_data":audio_data,
                "key_signatures":key_signature
            })
    else:
        pass
    
    return None
    
def export_sidebar(content):

    spotify = content["api_sources"]["spotify"]["track_list"]
    youtube = content["api_sources"]["youtube"]["track_list"]
    apple = content["api_sources"]["apple"]["track_list"]

    amazon = library.file.file_exists(content["api_sources"]["amazon"]["album_list"])
    advert = content["api_sources"]["karaoke_version"]["affiliate_link"]

    if spotify and youtube and apple and amazon and advert and content["url"]:

        library.comment.returnMessage("Processing Sidebar: "+content["url"])

        library.json.export_json(
            api_path+content["url"]+"/sidebar.json",
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
                "album_list":library.json.import_json(content["api_sources"]["amazon"]["album_list"]),
                "adverts":content["api_sources"]["karaoke_version"]["affiliate_link"]
            })


### Create Directories
www_export=[]

amazon=[]

library.comment.returnMessage("Start")



for content in library.json.import_json("Z:\\full_list.json"):

    if library.file.file_does_not_exists(api_path+content["url"]+"/profile.json"):
        export_profile(content)   

    if library.file.file_does_not_exists(api_path+content["url"]+"/sidebar.json") and library.file.file_exists(api_path+content["url"]+"/profile.json"):
        export_sidebar(content)
 
    if library.file.file_exists(api_path+content["url"]+"/profile.json") and library.file.file_exists(api_path+content["url"]+"/sidebar.json"):

        www_export.append({
                "artist":content["artist"],
                "track":content["track"],
                "url":content["url"]
        })
    

        

library.json.export_json(api_path+"/www.json",www_export)

library.comment.returnMessage("Complete")