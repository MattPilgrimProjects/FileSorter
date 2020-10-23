import app
import re

import library.cron

def parse_xml_data():

    root = app.xml.importXML("S:\Midi-Library\karaokeversion_catalog_en_GBP.xml")

    array=[]

    for artist in root.findall('./artist'):

        artist_name_tag = artist.find('name').text

        for songs in artist.iter('songs'):

            for song in songs.iter("song"):

                song_title_tag = song.find("name").text

                url = app.parser.find_and_replace_array(song.find("url").text,app.settings["xml_catalog"]["replace"])

                array.append({
                        "artist":library.parser.sanitize(artist_name_tag),
                        "track": library.parser.sanitize(song_title_tag),
                        "url": url,
                    })
    return array

artist_profile=[]
json_array=[]
writer = app.csv.createCSVHeader(app.settings["sources"]["track_list"]["csv"],["artist","track","url"])

for data in parse_xml_data():

    json_array.append(data)
    writer.writerow(data)
    pass

app.json.export_json(app.settings["sources"]["track_list"]["json"],json_array)