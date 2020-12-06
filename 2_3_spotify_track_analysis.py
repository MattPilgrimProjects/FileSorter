import app
import library.scan
import library.json
import library.url
import sys

track_database = app.settings["track_database"]
track_analysis_path = app.settings["spotify"]["track_analysis"]
export_path = app.settings["spotify"]["export"]


def get_track_analysis():
    for data in library.json.import_json(track_database):

        if library.file.file_exists(export_path+data["filename"]+".json"):
            for category, schema in library.json.import_json(export_path+data["filename"]+".json").items():

                if library.file.file_does_not_exists(track_analysis_path+data["filename"]+".json"):
                    if category == "tracks":
                        if schema["items"]:
                            track_id = schema["items"][0]["id"]
                            return_data = library.url.spotify_web_api(
                                "https://api.spotify.com/v1/audio-analysis/"+track_id, [], auth)
                            library.comment.returnUpdateMessage("Adding: "+track_analysis_path+data["filename"]+".json")
                            library.json.export_json(
                                track_analysis_path+data["filename"]+".json", return_data)

##############################################################


print("Enter the auth token:")
auth = "Bearer "+input()
library.comment.returnMessage("Start")
get_track_analysis()
library.comment.returnMessage("Completed")
