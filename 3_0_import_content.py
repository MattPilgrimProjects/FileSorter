import app
import config
import library.download

track_database = app.settings["track_database"]


def return_artist_list():
    artist_list = []

    for data in library.json.import_json(track_database):

        artist_list.append(config.import_html_content(data))

    return library.json.export_json("S:\\Midi-Library\\url\\search_by_artist.json", library.parser.remove_duplicates_from_dictionary(artist_list))


return_artist_list()
library.download.download_html("S:\\Midi-Library\\url\\search_by_artist.json")
