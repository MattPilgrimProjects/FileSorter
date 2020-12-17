import app
import config
import library.url
import library.json
import library.comment
import library.cron
import library.scan
import library.parser

import sys

live_path = app.settings["live_path"]

################################


def start_handler(line, config):

    line_count = line.split(config)

    if len(line_count) != 0:
        return line_count[1]
    else:
        return line


def end_handler(line, config):

    return line.split(config)[0]


def config_handler(line, config):

    if "start" in config and config["start"]:
        line = start_handler(line, config["start"])

    if "end" in config and config["end"]:
        line = end_handler(line, config["end"])
    
    line = library.parser.find_and_replace_array(line, config["find_and_replace"])

    if "split" in config:
        track_id = line.split("-")
        line = track_id[0]+"-"+track_id[1]
        

    return line


def export_handler(config):

    option = config["status"]
    source = config["source"]
    parse = config["filter"]
    split = config["filter_tags"]
    artist = config["artist"]
    track = config["track"]
    midipath = config["midi"]
    pagination = config["pagination"]

    library.comment.returnMessage("Importing web content from "+source)

    midi_list = []
    pagination_return = []

    for filename in library.scan.scan_file_recursively(live_path+source+"\\*.html"):

        localhost = filename.replace(
            live_path+source+"\\", "http://localhost/live/"+source+"/")

        a = library.parser.parseLinksFromHTML(localhost, parse)

        a = str(a)

        processed = a.split(split)

        artist_list = []
        track_list = []
        midi_path_list = []
        pagination_list = []

        for line in processed:

            if artist["match"] in line:
                artist_list.append(config_handler(line, artist))

            if track["match"] in line:
                track_list.append(config_handler(line, track))

            if midipath["match"] in line:
                midi_path_list.append(config_handler(line, midipath))

            if pagination and pagination["match"] in line:
                pagination_list.append(config_handler(line, pagination))

        profile = []

        if len(artist_list) == 1:
            for i in range(len(track_list)-1):
                artist_list.append(artist_list[0])

        if artist_list and track_list and midi_path_list:

            if len(artist_list) == len(track_list) == len(midi_path_list):

                for i in range(len(track_list)):

                    profile.append({
                        "artist": artist_list[i],
                        "track": track_list[i],
                        "midipath": midi_path_list[i]
                    })

                pass

        if pagination_list:
            pagination_return.extend(pagination_list)

        if option == "live":
            midi_list.extend(profile)

        if option == "dev":

            midi_list.append({
                "artist":artist_list,
                "track":track_list,
                "midi":midi_path_list
            })

    library.json.export_json("S:\\Midi-Library\\parsed\\pages\\"+source+".json", pagination_return)
    library.json.export_json("S:\\Midi-Library\\" +source+"\\midi-library.json", midi_list)

library.comment.returnMessage("Start")
# for data in config.data_extractor:
#     export_handler(data)
export_handler(config.data_extractor[3])
library.comment.returnMessage("Completed")