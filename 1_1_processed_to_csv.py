import app
import re

def processed_to_csv():
    stage = app.setup['stage']

    return_array=[]

    for schema in stage:

        file_array = app.scan.scan_file_recursively(schema["href_save_location"]+"*.html")

        for filename in file_array:
            
            keyword = filename.replace(schema["href_save_location"],"").replace(".html","")

            move_to = schema["processed_href"]["move_to"]+keyword+".csv"

            href_file = schema["href_save_location"]+keyword+".html"

            localhost = schema["localhost"]+keyword+".html"

            search_attribute = schema["processed_href"]["search_attribute"]

            match_array = schema["processed_href"]["match"]

            for link in app.parser.parseLinksFromHTML(localhost,search_attribute):

                for match in match_array:
        
                    if match in str(link):

                        data = str(link)

                        data = app.parser.regex(data,schema)

                        raw_data = data.strip()+"=>"+schema['title']

                        if app.parser.hasNumbers(raw_data) and raw_data!="":
                            return_array.append(raw_data) 
                               
                    pass
                
        pass     
    return return_array

src = app.parser.remove_duplicates_from_array(processed_to_csv())

writer = app.csv.createCSVHeader(app.settings["sources"]["midi_list"]["csv"],["href"])

return_array=[]

for data in src:

    data = app.parser.sanitize(data)

    writer.writerow({"href":data})
    
    return_array.append(data)
    

app.json.export_json(app.settings["sources"]["midi_list"]["json"],return_array)

app.comment.returnMessage("Completed"+app.settings["sources"]["midi_list"]["csv"])