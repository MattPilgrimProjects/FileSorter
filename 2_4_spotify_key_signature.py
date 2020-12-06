import app
import library.scan
import library.json
import library.file

import sys

track_anaylsis = app.settings["spotify"]["track_analysis"]
track_database = app.settings["track_database"]
key_signature = app.settings["spotify"]["key_signature"]

note_array = {
    9: "A",
    10: "A♯/B♭",
    11: "B",
    12: "C",
    13: "C♯/D♭",
    14: "D",
    15: "D♯/E♭",
    16: "E",
    17: "F",
    18: "F♯/G♭",
    19: "G",
    20: "G♯/A♭",
    21: "A",
    22: "A♯/B♭",
    23: "B",
    24: "C",
    25: "C♯/D♭",
    26: "D",
    27: "D♯/E♭",
    28: "E",
    29: "F",
    30: "F♯/G♭",
    31: "G",
    32: "G♯/A♭",
    33: "A",
    34: "A♯/B♭",
    35: "B",
    36: "C",
    37: "C♯/D♭",
    38: "D",
    39: "D♯/E♭",
    40: "E",
    41: "F",
    42: "F♯/G♭",
    43: "G",
    44: "G♯/A♭",
    45: "A",
    46: "A♯/B♭",
    47: "B",

}


def mode_relative_check(mode):

    mode_as_text = "No Result"

    if mode == 1:
        mode_as_text = "Minor"

    if mode == 0:
        mode_as_text = "Major"

    return mode_as_text


def mode_check(mode):

    mode_as_text = "No Result"

    if mode == 1:
        mode_as_text = "Major"

    if mode == 0:
        mode_as_text = "Minor"

    return mode_as_text


def note_check(note):

    note_as_text = ""

    for number, note_match in note_array.items():
        if note == number:
            note_as_text = note_match

    return note_as_text


def major_scale(root_note):

    major_scale_array = [0, 2, 4, 5, 7, 9, 11]

    array = []

    for sequence in major_scale_array:
        array.append(note_check(root_note+sequence))

    return array


def minor_scale(root_note):

    major_scale_array = [0, 2, 3, 5, 7, 8, 10]

    array = []

    for sequence in major_scale_array:
        array.append(note_check(root_note+sequence))

    return array


def array_return(filename):

    schema = library.json.import_json(track_anaylsis+data["filename"]+".json")

    try:
        schema["track"]
    except:
        library.comment.returnMessage(
            "Error on "+track_anaylsis+data["filename"]+".json")
        pass
    else:
        relative_note = ""

        if mode_check(schema["track"]["mode"]) == "Major":
            relative_note = schema["track"]["key"]+9
            key_signature_function = major_scale(schema["track"]["key"]+12)
            relative_scale = minor_scale(relative_note)

        if mode_check(schema["track"]["mode"]) == "Minor":
            relative_note = schema["track"]["key"]+15
            key_signature_function = minor_scale(schema["track"]["key"]+12)
            relative_scale = major_scale(relative_note)

        library.comment.returnMessage("Processing: "+filename)

        return {
            "key_signature": note_check(schema["track"]["key"]+12)+" "+mode_check(schema["track"]["mode"]),
            "relative_signature": note_check(relative_note)+" "+mode_relative_check(schema["track"]["mode"]),
            "time_signature": str(schema["track"]["time_signature"])+"/4",
            "key_signature_scale": key_signature_function,
            "relative_scale": relative_scale

        }


for data in library.json.import_json(track_database):

    if library.file.file_exists(track_anaylsis+data["filename"]+".json") and library.file.file_does_not_exists(key_signature+data["filename"]+".json"):
        library.json.export_json(key_signature+data["filename"]+".json", array_return(track_anaylsis+data["filename"]+".json"))
