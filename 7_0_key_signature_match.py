import app
import library.json
import library.midi
import library.comment
import library.file
import library.maths

track_database = app.settings["midi_library_database_file"]


def key_signature_match():

    for data in library.json.import_json(track_database):

        filename = data["filename"]

        filepath = "S:\\Midi-Library\\track_analysis\\"+filename+".json"

        if library.file.file_exists(filepath):
            pass
        else:

            key_signature_list = []

            for source, schema in data["sources"].items():

                for result in schema:
                    midi_filename = result["export"]
                    if library.midi.import_midi(midi_filename):
                        key_signature_list.append(
                            library.midi.clean(midi_filename))
                else:
                    pass

            data["content"] = key_signature_list

            library.comment.returnUpdateMessage(
                data["artist"]+" - "+data["track"])

            if data["key_signature"] and key_signature_list:

                library.json.export_json(filepath, data)


notes = [
    "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B", "C",
    "A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B", "C"

]


def major_scale(root_note):
    root_value = notes.index(root_note)
    result_export = []
    for i in [0, 2, 4, 5, 7, 9, 11]:
        result_export.append(notes[i+root_value])
    return result_export


def minor_scale(root_note):
    root_value = notes.index(root_note)
    result_export = []
    for i in [0, 2, 3, 5, 7, 8, 10]:
        result_export.append(notes[i+root_value])

    return result_export


def circle_of_fifths_segment(key, major, minor):
    if "Major" in key:

        return {
            "key_signature":key,
            "relative_signature":minor+" Minor",
            "main_scale": major_scale(major),
            "relative_scale": minor_scale(minor)
        }

    if "Minor" in key:

        return {
            "key_signature":key,
            "relative_signature":major+" Major",
            "main_scale": minor_scale(minor),
            "relative_scale": major_scale(major)
        }


def circle_of_fifths(key):

    if key == "C Major" or key == "A Minor":
        return circle_of_fifths_segment(key, "C", "A")

    if key == "G Major" or key == "E Minor":
        return circle_of_fifths_segment(key, "G", "E")

    if key == "D Major" or key == "B Minor":
        return circle_of_fifths_segment(key, "D", "B")

    if key == "A Major" or key == "F# Minor":
        return circle_of_fifths_segment(key, "A", "F#")

    if key == "E Major" or key == "C# minor":
        return circle_of_fifths_segment(key, "E", "C#")

    if key == "E Major" or key == "C# Minor":
        return circle_of_fifths_segment(key, "E", "C#")

    if key == "B Major" or key == "G# Minor":
        return circle_of_fifths_segment(key, "B", "G#")

    if key == "F# Major" or key == "D# Minor":
        return circle_of_fifths_segment(key, "F#", "D#")

    if key == "Db Major" or key == "Bb Minor":
        return circle_of_fifths_segment(key, "Db", "Bb")

    if key == "Ab Major" or key == "F Minor":
        return circle_of_fifths_segment(key, "Ab", "F")

    if key == "Eb Major" or key == "C Minor":
        return circle_of_fifths_segment(key, "Eb", "C")

    if key == "Bb Major" or key == "G Minor":
        return circle_of_fifths_segment(key, "Bb", "G")

    if key == "F Major" or key == "D Minor":
        return circle_of_fifths_segment(key, "F", "D")

    if key == "Eb Minor" or key == "Gb Major":
        return circle_of_fifths_segment(key, "Gb", "Eb")

    if key == "C# Major":
        return circle_of_fifths_segment(key, "C#", "Bb")


export_data = []
for data in library.json.import_json(track_database):
    # print(data)
    if data["key_signature"]:

        note = data["key_signature"][0]

        content = circle_of_fifths(note)

        

        library.json.export_json("S:\\Midi-Library\\key_signature\\"+data["filename"]+".json", content)
# library.json.export_json("S:\\Midi-Library\\key_signature\\api.json",export_data)

library.comment.returnMessage("Start")
# key_signature_match()
library.comment.returnMessage("Completed")
