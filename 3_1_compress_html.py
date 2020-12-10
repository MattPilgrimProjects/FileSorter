import app
import library.url
import library.json
import library.comment
import library.cron
import library.scan
import library.parser

import sys

live_path = app.settings["live_path"]

################################


def artist_handler(line, config):
    if config["start"]:
        line = line.split(config["start"])[1]
    if config["end"]:
        line = line.split(config["end"])[0]

    return library.parser.find_and_replace_array(line, config["find_and_replace"])


def export_handler(option, source, parse, split, artist, track, midipath, pagination):

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
                artist_list.append(artist_handler(line, artist))

            if track["match"] in line:
                track_list.append(artist_handler(line, track))

            if midipath["match"] in line:
                midi_path_list.append(artist_handler(line, midipath))

            if pagination and pagination["match"] in line:
                pagination_list.append(artist_handler(line, pagination))

        profile = []

        if len(artist_list) == 1:
            for i in range(len(track_list)-1):
                artist_list.append(artist_list[0])

        if artist_list and track_list and midi_path_list:

            if len(artist_list) == len(track_list) == len(midi_path_list):

                for i in range(len(track_list)):

                    if source == "freemidi":
                        midi_id = midi_path_list[i].split("-")
                        midi_path_list[i] = midi_id[0]+"-"+midi_id[1]

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
                # "raw": a,
                # "processed": processed,
                # "profile": profile,
                # "artist": artist_list,
                # "track": track_list,
                # "midi": midi_path_list,
                "pagination": pagination_list

            })

            pagination_return = library.parser.remove_duplicates_from_array(
                pagination_list)

    library.json.export_json("S:\\Midi-Library\\parsed\\pages\\"+source+".json", pagination_return)
    library.json.export_json("S:\\Midi-Library\\"+source+"\\midi-library.json", midi_list)


library.comment.returnMessage("Start")

export_handler("live", "mididb", "li", "\n",
               {
                   "match": "artist-name",
                   "start": ">",
                   "end": "</div>",
                   "find_and_replace": {
                       "</div": ""
                   }
               },
               {
                   "match": "player button blue",
                   "start": "title=",
                   "end": "itemprop",
                   "find_and_replace": {
                       '\"': "",
                       " MIDI backing track>": ""
                   }
               },
               {
                   "match": "data-audio-url",
                   "start": "data-audio-url",
                   "end": "</div>",
                   "find_and_replace": {
                       '=\"': "",
                       '\">': "",
                       "_prt.mp3": ".mid",
                       "https://www.mididb.com/midi-download/":"https://www.mididb.com/midi-download/AUD_"
                   }
               },
               {

               })

export_handler("live", "midiworld", "li", "<li>",
               {
                   "match": "download",
                   "start": "(",
                   "end": ")",
                   "find_and_replace": {

                   }
               },
               {
                   "match": "download",
                   "start": "\n",
                   "end": " (",
                   "find_and_replace": {

                   }
               },
               {
                   "match": "download",
                   "start": '<a href=\"',
                   "end": '\" target=',
                   "find_and_replace": {


                   }
               }, {})


# export_handler("live", "freemidi", "a", "</a>",
#                {
#                    "match": '.org/artist-',
#                    "start": 'e\">',
#                    "end": "</span>",
#                    "find_and_replace": {

#                    }
#                },
#                {
#                    "match": "download3-",
#                    "start": '\n',
#                    "end": '',
#                    "find_and_replace": {

#                    }
#                },
#                {
#                    "match": "download3-",
#                    "start": 'href=\"',
#                    "end": '\"',
#                    "find_and_replace": {
#                        "download3-": "https://freemidi.org/getter-"
#                    }
#                },
#                {
#                    "match": "-P-",
#                    "start": '<a href=\"',
#                    "end": '\"',
#                    "find_and_replace": {
#                        "https://freemidi.org/": ""
#                    }

#                })

library.comment.returnMessage("Completed")
