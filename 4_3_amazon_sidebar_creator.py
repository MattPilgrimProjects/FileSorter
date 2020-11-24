import app
import library.scan
import library.parser
import library.json

for filename in library.scan.scan_file_recursively("S:\\Website Projects\\api\\*\\*\\profile.json"):

    match_title = library.parser.find_and_replace_array(filename,{
        "S:\\Website Projects\\api\\":"",
        "\\profile.json":"",
        "\\":"-"
    })

    array=[]
    for return_filename in library.scan.scan_file_recursively("S:\\Midi-Library\\amazon\\processed\\"+match_title+"*.json"):
        for data in library.json.import_json(return_filename):
            array.append(data)
        pass

    if array:
        library.json.export_json("S:\\Midi-Library\\amazon\\sidebar\\"+match_title+".json",array)
    