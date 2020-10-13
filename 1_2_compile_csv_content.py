import app

def compile_csv_content():

    for schema in app.setup['stage']:
        
        for keyword in return_keywords_from_processed_list(schema):
               
               process_href = schema["processed_href"]["move_to"]+keyword+".csv"

               array=[]

               if app.file.file_exists(process_href):

                for csv_row in app.csv.importCSVData(process_href):

                    if csv_row[0]!="href" and app.parser.hasNumbers(csv_row[0]):

                        data = app.parser.regex(csv_row[0],schema)

                        raw_data = data.strip()+"=>"+schema['title']

                        if data!="":
                            array.extend([raw_data])

                array = app.parser.remove_duplicates_from_array(array)
                app.comment.returnMessage(schema['raw_keywords_json']+"\\"+keyword+".json")
                app.json.export_json(schema['raw_keywords_json']+"\\"+keyword+".json",array)

            



def return_keywords_from_processed_list(schema):

    keyword_array = []

    for filename in app.scan.scan_file_recursively(schema["processed_href"]["move_to"]+"\\*"):

        keyword = app.parser.find_and_replace_array(filename,{
           schema["processed_href"]["move_to"]:"",
            ".csv":""
        })

        keyword_array.append(keyword)

    return keyword_array


app.comment.returnMessage("Start Search")
compile_csv_content()