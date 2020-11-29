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

    if library.file.file_exists("S:\\Website Projects\\live\\freemidi\\"+string+".html"):
        return "match"

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

    if medium and low:
        return {
            "high":medium,
            "low":low
        
        }
    else:
        return "no match"

def artist_list_return():
    artist_list=[]
    for artist in library.json.import_json("Z:\\sources\\track_list.json"):

        if library.file.file_does_not_exists("S:\\Website Projects\\live\\freemidi\\"+artist["filename_artist"]+".html"):
            artist_list.append(artist["filename_artist"])
        pass
    
    return library.parser.remove_duplicates_from_array(artist_list)

def artist_match_algorithm():

    artist_list = artist_list_return()

    return_array=[]

    for url in library.json.import_json("Z:\\parsed\\dev\\freemidi_search.json"):

        remove_artist_id = url.replace("https://freemidi.org/artist-","").split("-")[0]

        data = url.replace("https://freemidi.org/artist-"+remove_artist_id+"-","")

        stats=match_amount_high(data,artist_list)

        if stats in ["no match","match"]:
            pass
        else:
            return_array.append({
                    "match":data,
                    "url":url,
                    "stats":stats,
                            
            })
    
        
    library.json.export_json("Z:\\parsed\\dev\\match.json",return_array)


def import_artist_profile():

    for data in library.json.import_json("Z:\\parsed\\dev\\match.json"):
        if isinstance(data["stats"], str) and library.file.file_does_not_exists("S:\\Website Projects\\live\\freemidi\\"+data["stats"]+".html"): 
            library.url.download_html_content(data["url"],"S:\\Website Projects\\live\\freemidi\\"+data["stats"]+".html")
         


#################################

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

library.comment.returnMessage("Import artist profile")

library.comment.returnMessage("Match artist to database")
import_artist_profile()
artist_match_algorithm()
import_artist_profile()

library.comment.returnMessage("Completed")