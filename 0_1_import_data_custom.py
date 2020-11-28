import app
import library.url
import library.json
import library.comment
import library.cron
import library.scan
import library.parser

import sys

################################

def artist_handler(line,config):
    line = line.split(config["start"])[1]
    line = line.split(config["end"])[0]
    return library.parser.find_and_replace_array(line,config["find_and_replace"])

def export_handler(option,source,parse,split,midipath):

    library.comment.returnMessage("Importing web content from "+source)

    midi_list=[]

    for filename in library.scan.scan_file_recursively("S:\\Website Projects\\live\\"+source+"\\*.html"):

        localhost = filename.replace("S:\\Website Projects\\live\\"+source+"\\","http://localhost/live/"+source+"/")

        a = library.parser.parseLinksFromHTML(localhost,parse)

        a = str(a)

        processed = a.split(split)


        midi_path_list=[]
        for line in processed:

 
            if midipath["match"] in line:
                midi_path_list.append(artist_handler(line,midipath))

        #Top two lines are for dev work

        profile=[]

        if midi_path_list:

            if len(midi_path_list):

                
                for i in range(len(midi_path_list)):
                    profile.append(midi_path_list[i])
                
                pass
            
        if option =="live":
            midi_list.extend(profile)
            midi_list = library.parser.remove_duplicates_from_array(midi_list)
        
        if option =="dev":

            midi_list.append({
                    "raw":a,
                    "processed":processed,
                    "profile":profile
                        
            })
    return library.json.export_json("Z:\\parsed\\dev\\"+source+".json",midi_list)


def match_amount_high(string,array):

    high=[]
    medium=[]

    low=[]

    for data in array:

        if library.parser.low_match_percentage(string,data) >= 50:
            low.append({data:library.parser.low_match_percentage(string,data)})

        if library.parser.high_match_percentage(string,data) == 100.0:
            return data
        
        elif library.parser.high_match_percentage(string,data) >= 80.0:
            medium.append({data:library.parser.high_match_percentage(string,data)})
        else:
            pass

    return {
        "high":medium,
        "low":low
     
    }


library.comment.returnMessage("Start")



# export_handler("live","freemidi_search","a","</a>",
# {
#     "match":"/artist-",
#     "start":'href=\"',
#     "end":'\">',
#     "find_and_replace":{
#         "/artist":"https://freemidi.org/artist"
#     }
# })

## Create song track per artist

library.comment.returnMessage("Create song track per artist")

artist_list=[]
for artist in library.json.import_json("Z:\\sources\\artist_list.json"):
    artist_list.append(library.parser.change_to_url(artist))
    
    pass

return_array=[]

for url in library.json.import_json("Z:\\parsed\\dev\\freemidi_search.json"):

    rename = url.replace("https://freemidi.org/","S:\\Website Projects\\live\\freemidi\\")+".html"

    remove_artist_id = url.replace("https://freemidi.org/artist-","").split("-")[0]

    data = url.replace("https://freemidi.org/artist-"+remove_artist_id+"-","")

    stats=match_amount_high(data,artist_list)

    return_array.append({
                "match":data,
                "url":url,
                "stats":stats,
                
    })

    if data == stats and library.file.file_does_not_exists(rename):
        library.url.download_html_content(url,rename)
 

    library.comment.returnMessage("Processing: "+data)



library.json.export_json("Z:\\parsed\\dev\\match.json",return_array)