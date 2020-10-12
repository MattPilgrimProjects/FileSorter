import app
import re
import schedule
import time

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


##########################################################################################
def compile_csv_content():

    keyword = app.random_keyword()

    for schema in stage:

        process_href = schema["processed_href"]["move_to"]+keyword+".csv"

        if app.file.file_exists(process_href):

            csv_file = app.csv.importCSVData(process_href)

            for csv_row in csv_file:

                if csv_row[0]!="href" and hasNumbers(csv_row[0]):

                    data = regex(csv_row[0],schema)

                    raw_data = data.strip()+"=>"+schema['title']

                    if data!="":

                        array.extend([raw_data])
                        

                pass

            array = app.parser.remove_duplicates_from_array(array)

            app.json.export_json(schema['raw_keywords_json']+"\\"+keyword+".json",array)
            app.comment.returnMessage("Completed =>"+keyword)
        else:
            app.comment.returnMessage("Keyword not found =>" +keyword)
    return True



schedule.every(5).seconds.do(compile_csv_content)

while 1:
    schedule.run_pending()
    time.sleep(1)