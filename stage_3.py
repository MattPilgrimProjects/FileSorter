import app
import library.json
import library.csv
import library.comment
import library.scan
import re



stage = app.setup['stage']

search_database = app.setup["search_database"]

array=[]

library.comment.returnMessage("Start Search")

def regex(data):
    regex = re.compile('[^a-z- =0-9()A-Z]')
    
    return regex.sub('', data.split(trim, 1)[0])


for schema in stage:

    process_href = schema["processed_href"]["move_to"]

    for filename in library.scan.scan_file_recursively(process_href+"*.csv"):

        csv_file = library.csv.importCSVData(filename)

        for csv_row in csv_file:

            if csv_row[0]!="href":

                data = csv_row[0]

                remove_array = schema["processed_href"]["remove"]

                for remove in remove_array:

                    data = data.replace(remove,"")

                pass

            
                

                trim = schema["processed_href"]["trim"]

                title = schema["title"]

                array.append({
                    "title":title,
                    "keyword":filename.replace(process_href,"").replace(".csv",""),
                    "raw":regex(data)
                })

        pass

library.json.export_json(search_database,array)

library.comment.returnMessage(search_database)

library.comment.returnMessage("Completed")


