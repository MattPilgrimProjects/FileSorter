import library.json
import random

setup = library.json.import_json("settings.json")

settings = library.json.import_json("settings.json")


def import_config(filename):
    return library.json.import_json(filename)


def app_setup(number):

    return setup['midi_library']['preset_1']


def track_database():
    return setup['track_database']


def regex_filter():
    return setup['regex_filters']


