import library.parser
import library.comment
import library.json
import library.file
import library.scan

def check_value_against_list(data,artist_list):

    artist_match_list = []

    for check_artist in artist_list:

        high = library.parser.high_match_percentage(check_artist, data)

        if high >= 80.0:
            artist_match_list.append((check_artist, high))

   
    return library.parser.convert_tuples_to_dictionary(artist_match_list)

def match_by_percentage(value_1,value_2):
    return library.parser.high_match_percentage(value_1, value_2)

def run_matching_algorithm(input_data,output_filepath):

    filedata = library.scan.scan_directory(app.settings["library_path"]+"\\karaoke_version\\processed\\",output_filepath+"processed\\")    

    for results in filedata["data"]:

        if results["file_exists"]==False and library.file.file_does_not_exists(output_filepath+"high_match\\"+results["filename"]):

            original_data = library.json.import_json(results["filepath"])
            check_uncompressed_list = library.json.import_json(input_data)

            high_match=[]
            low_match=[]
            output_handler=[]

            for schema in check_uncompressed_list:
                
                match_artist =match_by_percentage(original_data["artist"],schema["artist"])
                match_track = match_by_percentage(original_data["track"],schema["track"])
                

                output_handler= schema
                output_handler.update({
                    "match_percentage":{
                            "artist":match_artist,
                            "track":match_track
                        }
                })
                

                if match_artist >=75 and match_track >=75:

                    high_match.append(output_handler)

                elif match_artist >=50 and match_track >=50:

                    low_match.append(output_handler) 
                else:
                    pass        

            if high_match:
                library.json.export_json(output_filepath+"high_match\\"+results["filename"],{
                    "original":original_data,
                    "data_match":high_match
                })
            
            if low_match:
                library.json.export_json(output_filepath+"low_match\\"+results["filename"],{
                    "original":original_data,
                    "data_match":low_match
                })

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
            library.comment.returnUpdateMessage(str(results["file_does_not_exist_count"])+"/"+filedata["file_does_not_exist_count"])

def run_processed_algorithm(filepath):
    for filename in library.scan.scan_file_recursively(filepath+"high_match\\*.json"):

        for title,filedata in library.json.import_json(filename).items():

            if title=="original":
                original = filedata

            if title=="data_match":

                array=[]

                for data in filedata:

                    array.append(data)

                    if data["match_percentage"]["artist"]==100.0 and data["match_percentage"]["track"] > 90.0 or data["match_percentage"]["artist"] > 90.0 and data["match_percentage"]["track"] ==100.0:           
                        
                        library.json.export_json(filepath+"processed\\"+original["filename"]+".json",{
                                "original":original,
                                "data_match":array
                        })

                        library.comment.returnMessage("Processing Matches: "+original["filename"])                         
