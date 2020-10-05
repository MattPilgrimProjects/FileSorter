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

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def regex(data,schema):

    trim = schema["processed_href"]["trim"]

    data = data.split(trim, 1)[0]

    # regex = re.compile('[^a-z- =0-9()A-Z]')
    
    # data = regex.sub('', )

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

    for filename in library.scan.scan_file_recursively(process_href+"*.csv"):

        csv_file = library.csv.importCSVData(filename)

        for csv_row in csv_file:

            if csv_row[0]!="href" and hasNumbers(csv_row[0]):

                data = regex(csv_row[0],schema)

                if data!="":
                    array.append(data.strip()+" ="+schema['title'])
                

        pass

array = library.parser.remove_duplicates_from_array(array)

library.json.export_json(search_database,array)

library.comment.returnMessage(search_database)

library.comment.returnMessage("Completed")


