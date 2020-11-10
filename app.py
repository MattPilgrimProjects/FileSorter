import library.json
import library.parser


setup = library.json.import_json("S:\\Projects\\settings.json")

settings = library.json.import_json("S:\\Projects\\settings.json")


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
