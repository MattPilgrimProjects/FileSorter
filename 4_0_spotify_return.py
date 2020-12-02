import app
import library.file
import library.json
import library.cron
import library.url
import library.comment
import library.scan

print("Enter the auth token:")
auth = "Bearer "+input()

for filename in library.scan.scan_file_recursively("S:\\Website Projects\\MusicKeyFinder\\resources\\api\\*\\*\\profile.json"):

    api = library.parser.global_return_path(filename) 

    for key,data in library.json.import_json(filename).items():
        if key=="artist": artist = data
        if key=="track" :  track= data
    

    if library.file.file_exists("Z:\\spotify\\raw_data\\"+api["sources"]):
        pass
    else:
        params = (
            ('q', artist+" "+track),
            ('type', 'track,artist'),
            ('limit', '20'),
            ('market','US'),
            ('include_external','audio')
        )
        library.cron.delay(1)
        content = library.url.spotify_web_api("https://api.spotify.com/v1/search",params,auth)
        if content:
            library.comment.returnMessage("Processing "+filename)
            library.json.export_json(filename,content)
            library.comment.returnMessage("Added "+filename)
        else:
            pass
