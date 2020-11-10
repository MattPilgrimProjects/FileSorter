import app
import library.file
import library.json
import library.directory

def export_file(album_list,api_output,spotify_return,youtube_return,apple_music_return):

    if library.file.file_exists(album_list):
        library.json.export_json(api_output+"/sidebar.json",{
            "playback":{
                "spotify":spotify_return,
                "youtube":youtube_return,
                "apple_music":apple_music_return
                },
            "album_list":library.json.import_json(album_list)
        })
    else:
        pass


def check_file_exists(file):

    if library.file.file_exists(file):
        return library.json.import_json(file)
    else:
        return {
            "href":""
        }


for schema in library.json.import_json(app.settings["www"]):

    api_output = app.settings["live_api"]+schema['url']

    filename = library.parser.create_filename(schema["url"])

    album_list = app.settings["spotify"]["album_list"]+filename

    spotify = app.settings["spotify"]["track_list"]+filename

    youtube = app.settings["youtube"]["track_list"]+filename

    apple_music = app.settings["apple_music"]["track_list"]+filename

    spotify_return = check_file_exists(spotify)
    youtube_return = check_file_exists(youtube)
    apple_music_return = check_file_exists(apple_music)

    export_file(album_list,api_output,spotify_return,youtube_return,apple_music_return)
    # if library.file.file_exists(api_output+"/sidebar.json"):
    #     pass
    # else:

        # else:
        #     pass
    

