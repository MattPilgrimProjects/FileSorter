import app
import library.csv
import library.parser
import library.json
import library.file


def export_csv_content(csv_file,json_file):

    for csv_row in library.csv.import_csv(csv_file):

        href=csv_row[2].split("/")

        if href[0] !="url":

            filepath = json_file+href[1]+"-"+href[2]+".json"

            if library.file.file_exists(filepath) or csv_row[3]=="click":
                pass
            else:
                library.json.export_json(filepath,{
                    "href":csv_row[3]
                })
                library.comment.returnMessage("Added: "+filepath)

export_csv_content("Z://AppleMusic.csv","Z:\\apple_music\\track_list\\")   
export_csv_content("Z://YouTube.csv","Z:\\youtube\\track_list\\")   
