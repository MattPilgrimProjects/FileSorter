import app
import library.scan 
import library.file
import library.parser
import library.csv
import library.comment

def processed_to_csv(filename,schema):

    return_array=[]

    search_attribute = schema["processed_href"]["search_attribute"]

    match_array = schema["processed_href"]["match"]

    for link in library.parser.parseLinksFromHTML(filename,search_attribute):

        for match in match_array:
        
            if match in str(link):

                data = str(link)

                data = library.parser.regex(data,schema)

                raw_data = data.strip()+"=>"+schema['title']

                if library.parser.hasNumbers(raw_data) and raw_data!="":
                    return_array.append(raw_data) 
                               
                pass
                    
    return return_array

return_array=[]

library.comment.returnMessage("Start")

for schema in app.settings["stage"]:

    file_array = library.scan.scan_file_recursively(schema["href_save_location"]+"*.html")

    for filename in file_array:

        localhost = filename.replace(schema["href_save_location"],schema["localhost"])

        csv_filename = library.parser.find_and_replace_array(filename,{
            schema["href_save_location"] : schema["keywords"]["output"]["csv"],
            ".html":".csv"
        })


        if library.file.file_does_not_exists(csv_filename) and library.file.file_exists(filename):

            body=[]

            for value in library.parser.remove_duplicates_from_array(processed_to_csv(localhost,schema)):
                body.append({"href":value})

            library.csv.export_csv(csv_filename,["href"],body)
            library.comment.returnUpdateMessage("Processing")
        else:
            pass

    pass

pass

library.comment.returnMessage("Completed")