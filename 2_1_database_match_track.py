import app
import library.json
import library.scan
import library.parser
import library.file
import library.comment
import library.cron
import library.directory
import library.url



def return_tracks_from_database(artist_array):

    export_location = app.settings["sources"]["track_list"]["json"]

    array=[]
    
    for row in library.json.import_json(export_location):

        if row["artist"] in artist_array:
            array.append(row["track"])  
        else:
            pass   
    
    return library.parser.remove_duplicates_from_array(array)


def output_handler(return_track,row,high_percentage_match,low_percentage_match):
    return{
            "raw_artist":row['artist'],
            "track":return_track,
            "raw_track":row["track"],
            "url":row["download_url"],
            "high":high_percentage_match,
            "low":low_percentage_match
    }

def percentage_matcher_module(filename,artist_list):

    perfect_match_array=[]
    high_match_array=[]
    medium_match_array=[]

    for row in library.json.import_json(filename):
       
        for return_track in artist_list:

            low_percentage_match = library.parser.low_match_percentage(row["track"],return_track)
            high_percentage_match = library.parser.high_match_percentage(row["track"],return_track)  

            if high_percentage_match == 100.0 and low_percentage_match==100.0:

                    perfect_match_array.append(output_handler(return_track,row,high_percentage_match,low_percentage_match))

            elif high_percentage_match >= 90:
                    
                    high_match_array.append(output_handler(return_track,row,high_percentage_match,low_percentage_match))

            elif high_percentage_match >= 80:

                    medium_match_array.append(output_handler(return_track,row,high_percentage_match,low_percentage_match))
            else:
                pass
    return {
        "perfect":perfect_match_array,
        "high":high_match_array,
        "medium":medium_match_array
    }

def file_output_setup(level,filename,artist_list):

    create_artist_directory = filename.replace(".json","\\").replace(filename,"S:\\Midi-Library\\tracks\\freemidi")

    if library.file.file_exists(create_artist_directory+level+".json"):
        pass
    elif percentage_matcher_module(filename,artist_list)[level]:  
        library.directory.create_recursive_directory(create_artist_directory) 
        library.json.export_json(create_artist_directory+level+".json",percentage_matcher_module(filename,artist_list)[level])
        library.comment.returnMessage("Completed: " + create_artist_directory+level+".json")
    else:
        pass

def load(alphabet):
    artistList=[]

    for row in library.scan.import_json_from_directory_recursively("S:\\Midi-Library\\artist\\freemidi\\processed\\"+alphabet+"_*.json"):
        artistList.append(row["artist"])

    artist_array = return_tracks_from_database(artistList)

    for filename in library.scan.scan_file_recursively("S:\\Midi-Library\\tracks\\freemidi\\"+alphabet+"\\artist-*.json"):

        file_output_setup("perfect",filename,artist_array)
        file_output_setup("high",filename,artist_array)
        file_output_setup("medium",filename,artist_array)

##########################################################################################################################

for alphabet in ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]:

    load(alphabet)


##########################################################################################################################
    
