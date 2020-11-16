import app
import library.csv
import library.parser
import library.json
import library.file

for csv_row in library.csv.import_csv("Z://AppleMusic.csv"):

    href=csv_row[2].split("/")

    if href[0] !="url":

        filepath = "Z:\\apple_music\\track_list\\"+href[1]+"-"+href[2]+".json"

        if library.file.file_exists(filepath) or csv_row[3]=="click":
            pass
        else:
            library.json.export_json(filepath,{
                "href":csv_row[3]
            })
            library.comment.returnMessage("Added: "+filepath)

   