import app
import re

stage = app.setup['stage']

search_database = app.setup["search_database"]

array=[]

app.comment.returnMessage("Start Search")

def midiworld(schema,data):

    track = schema.split(" (")[0]

    artist = schema.replace(track+" (","").split(")")[0]

    url = "/"+artist.replace(" ","-").lower()+"/"+track.replace(" ","-").lower()

    track_id = schema.replace(" ("+artist+") - ","").replace(" =midiworld","").replace(track,"")

    return output_handler(data["artist"],data["track"],"midiworld",track_id,url)

def output_handler(artist,track,source,track_id,url):
    return {
        "artist":artist,
        "track":track,
        "source":source,
        "track_id":track_id,
        "url": url,
    } 

def freemidi(schema,data):

    schema = schema.replace("=freemidi","").lower()

    track_id = schema.split("-")[0]

    track = schema.split(" ")[0].replace(track_id+"-","")
    
    track = schema.replace(track,"").replace(track_id+"- ","").strip().replace(" ","-")

    artist = schema.split(" ")[0].replace(track_id+"-","").replace(track+"-","")

    url = "/"+artist+"/"+track

    return output_handler(data["artist"],data["track"],"freemidi",track_id,url)

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

for schema in stage:

    process_href = schema["processed_href"]["move_to"]

    for filename in app.scan.scan_file_recursively(process_href+"*.csv"):

        csv_file = app.csv.importCSVData(filename)

        for csv_row in csv_file:

            if csv_row[0]!="href" and hasNumbers(csv_row[0]):

                data = regex(csv_row[0],schema)

                raw_data = data.strip()+"=>"+schema['title']

                if data!="":

                    array.extend([raw_data])
                

        pass

array = app.parser.remove_duplicates_from_array(array)

app.json.export_json(search_database,array)

app.comment.returnMessage(search_database)

app.comment.returnMessage("Completed")
