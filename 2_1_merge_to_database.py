import library.file
import library.machine_learning
import sys
import app
import config

import library.scan
import library.json


def create_midi_database():
    export_dictionary = []

    for filename in library.scan.scan_file_recursively("S:\\Midi-Library\\mididb\\unprocessed\\*.json"):

        artist_list = []
        track_list = []
        midi_list = []

        for data in library.json.import_json(filename):

            if "artist" in data:
                artist_list.extend(data["artist"])
            if "track" in data:
                track_list.extend(data["track"])
            if "midi" in data:
                midi_list.extend(data["midi"])

        if len(artist_list) == len(track_list):

            for i in range(len(artist_list)):

                export_dictionary.append({
                    "artist": artist_list[i],
                    "track": track_list[i],
                    "midi": midi_list[i]
                })

    return library.json.export_json("S:\\Midi-Library\\mididb\\midi-library.json", library.parser.remove_duplicates_from_dictionary(export_dictionary))


def create_key_signature_database():
    export_dictionary = []

    for filename in library.scan.scan_file_recursively("S:\\Midi-Library\\musicnotes\\unprocessed\\*.json"):

        artist_list = []
        track_list = []
        key_signature_list = []

        for data in library.json.import_json(filename):

            if "artist" in data:
                artist_list.extend(data["artist"])
            if "track" in data:
                track_list.extend(data["track"])
            if "key_signature" in data:
                key_signature_list.extend(data["key_signature"])

        if len(artist_list) == len(track_list):

            for i in range(len(artist_list)):

                export_dictionary.append({
                    "artist": artist_list[i],
                    "track": track_list[i],
                    "key_signature": key_signature_list[i]
                })

    return library.json.export_json("S:\\Midi-Library\\musicnotes\\key-signature.json", library.parser.remove_duplicates_from_dictionary(export_dictionary))


def create_pagination_database():
    lst = []
    for filename in library.scan.scan_file_recursively("S:\\Midi-Library\\freemidi\\unprocessed\\*.json"):

        pagination_list = []

        for data in library.json.import_json(filename):

            if "pagination" in data:
                pagination_list.extend(data["pagination"])

        for url in pagination_list:

            lst.append({
                "import": url,
                "export": "S:\\Website Projects\\live\\freemidi\\"+handler(url)
            })

    return library.json.export_json("S:\\Midi-Library\\freemidi\\pagination.json", library.parser.remove_duplicates_from_dictionary(lst))


def handler(value):

    value = value.replace("https://freemidi.org/artist-", "")

    track_id = value.split("-")[0]+"-"

    return value.replace(track_id, "")+".html"

# create_midi_database()

# create_key_signature_database()


# create_pagination_database()

original_track_list = app.settings["karaokeversion"]["compressed"]


def run_matching_algorithm(import_filepath, export_filepath):

    for data in library.json.import_json(original_track_list):

        filename = data["filename_artist"]+"-"+data["filename_track"]

        if library.file.file_does_not_exists(export_filepath+filename+".json"):

            schema_list = []

            for schema in library.json.import_json(import_filepath):

                match_artist = library.machine_learning.match_by_percentage(
                    data["artist"], schema["artist"])
                match_track = library.machine_learning.match_by_percentage(
                    data["track"], schema["track"])

                if match_artist >= 75 and match_track >= 75:

                    schema_list.append({
                        "artist": schema["artist"],
                        "track": schema["track"],
                        "key_signature": schema["key_signature"],
                        "match_percentage":
                        {
                            "artist": match_artist,
                            "track": match_track
                        }

                    })

            if schema_list:
                library.comment.returnUpdateMessage(
                    "Processing "+data["artist"] + " - "+data["track"])

                library.json.export_json(export_filepath+filename+".json", {
                    "original": data,
                    "musicnote_check": schema_list
                })

    return "Completed"


run_matching_algorithm("S:\\Midi-Library\\musicnotes\\key-signature.json","S:\\Midi-Library\\musicnotes\\key_signature\\")
