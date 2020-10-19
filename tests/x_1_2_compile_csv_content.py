import app
def midiworld(schema,data):

        track = schema.split(" (")[0]

        artist = schema.replace(track+" (","").split(")")[0]

        url = "/"+artist.replace(" ","-").lower()+"/"+track.replace(" ","-").lower()

        track_id = schema.replace(" ("+artist+") - ","").replace("=>midiworld","").replace(track,"")

        return{
        "artist":data["artist"],
        "track":data["track"],
        "source":"midiworld",
        "track_id":track_id,
        "url": url,
        }

def freemidi(schema,data):

    schema = schema.replace("=>freemidi","").lower()

    track_id = schema.split("-")[0]

    track = schema.split(" ")[0].replace(track_id+"-","")
    
    track = schema.replace(track,"").replace(track_id+"- ","").strip().replace(" ","-")

    artist = schema.split(" ")[0].replace(track_id+"-","").replace(track+"-","")

    return{
        "artist":data["artist"],
        "track":data["track"],
        "source":"freemidi",
        "track_id":track_id,
        "url": "/"+artist+"/"+track
        }

def compile_csv_content():

    export_array=[]

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
                            export_array.append(raw_data)
                            

      
                # array = app.parser.remove_duplicates_from_array(array)
                # app.comment.returnMessage("Completed: "+schema['raw_keywords_json']+keyword+".json")
                # app.json.export_json(schema['raw_keywords_json']+keyword+".json",array)

            else:
                pass       
    return export_array

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



src = app.parser.remove_duplicates_from_array(compile_csv_content())

writer = app.csv.createCSVHeader("Z:\\sources\\midi_list.csv",["artist","track","source","track_id","url"])

for data in src:
    writer.writerow({"src":data})
    pass

app.json.export_json("Z:\\sources\\midi_list.json",src)




