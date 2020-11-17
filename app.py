import library.json
import library.parser


setup = library.json.import_json("P:\\settings.json")

settings = library.json.import_json("P:\\settings.json")

directory_import_path = settings["source"]["freemidi"]["directory"]["import"]

artist_download_path = settings["source"]["freemidi"]["artist"]["download"]
artist_import_path = settings["source"]["freemidi"]["artist"]["import"]
artist_localhost_path = settings["source"]["freemidi"]["artist"]["localhost"]
artist_library_path = settings["source"]["freemidi"]["artist"]["library"]
artist_processed_path = settings["source"]["freemidi"]["artist"]["processed"]
artist_pagination_list = settings["source"]["freemidi"]["artist"]["pagenation"]

track_library_path = settings["source"]["freemidi"]["tracks"]["library"]
track_import_path = settings["source"]["freemidi"]["tracks"]["import"]


midi_download_path = settings["source"]["freemidi"]["midi"]["download"]
midi_library_path = settings["source"]["freemidi"]["midi"]["library"]
midi_processed_path = settings["source"]["freemidi"]["midi"]["processed"]

export_location = settings["sources"]["track_list"]["json"]


def import_config(filename):
    return library.json.import_json(filename)


def app_setup(number):

    return setup['midi_library']['preset_1']


def track_database():
    return setup['track_database']


def regex_filter():
    return setup['regex_filters']


def random_keyword():
    keywords_array = library.json.import_json(settings["keyword_list_export"]["compressed"])
    return library.parser.return_random_array_value(keywords_array)
