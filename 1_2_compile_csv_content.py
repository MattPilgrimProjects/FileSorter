import app
import re

stage = app.setup['stage']

search_database = app.setup["search_database"]

array=[]

app.comment.returnMessage("Start Search")

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def regex(data,schema):

    trim = schema["processed_href"]["trim"]

    data = data.split(trim, 1)[0]

    if schema["processed_href"]["match"] in data:
        return_data = data
    else:
        return_data = ""
        pass


    for remove in schema["processed_href"]["remove"]:

        return_data = return_data.replace(remove,"")

    
    return return_data

for schema in stage:

    process_href = schema["processed_href"]["move_to"]

    for filename in app.scan.scan_file_recursively(process_href+"*.csv"):

        csv_file = app.csv.importCSVData(filename)

        for csv_row in csv_file:

            if csv_row[0]!="href" and hasNumbers(csv_row[0]):

                data = regex(csv_row[0],schema)

                raw_data = data.strip()+" ="+schema['title']

                if data!="" and raw_data not in app.json.import_json("Z:\\raw_href\\processed.json"):
                    
                    array.extend([raw_data])
                

        pass

array = app.parser.remove_duplicates_from_array(array)

app.json.export_json(search_database,array)

app.comment.returnMessage(search_database)

app.comment.returnMessage("Completed")
