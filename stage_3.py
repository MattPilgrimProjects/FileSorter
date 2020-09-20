import app
import library.json
import library.csv
import library.comment
import re

keyword = app.setup["keyword"]

stage = app.setup['stage']

search_database = app.setup["search_database"]

array=[]

for schema in stage:

    processed_csv_file = schema["processed_href"]["move_to"]+keyword+".csv"

    title = schema["title"]

    remove_array = schema["processed_href"]["remove"]

    csv_file = library.csv.importCSVData(processed_csv_file)

    trim = schema["processed_href"]["trim"]

    for csv_row in csv_file:

        if csv_row[0]!="href":

            data = csv_row[0]

            for remove in remove_array:


                data = data.replace(remove,"")

                pass

            
            regex = re.compile('[^a-z- =0-9()A-Z]')
     

            array.append({
                "title":title,
                "keyword":keyword,
                "raw":regex.sub('', data.split(trim, 1)[0])
                })

        pass


library.json.export_json(search_database,array)

library.comment.returnMessage(search_database)


