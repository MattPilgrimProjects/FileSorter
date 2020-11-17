import app
import library.scan 
import library.comment
import library.file
import controllers.return_key_signature

from scipy import stats

diatonic_scale=library.json.import_json("Z:\\circle_of_fifths.json")

def return_key_signature(filename):

    file_content = library.json.import_json(filename)

    midi_channels = library.json.import_json("P:\\midi.json")

    full_chord_array=[]
    full_notes_list=[]
    return_all_notes=[]
    full_list_of_notes_after_max_found=[]

    for channel,note_array in file_content.items():

        channel = channel

        most_used_note_array=[]

        for note,count in note_array.items():
            most_used_note_array.append(int(count))
            pass

        

        if most_used_note_array:

            for note,count in note_array.items():
                if int(count) == max(most_used_note_array):
        
                    full_list_of_notes_after_max_found.append(midi_channels[note])

    
            pass


        most_common_scale=[]

        midi_list=[]

        for note,count in note_array.items():  

            full_notes_list.append(note)

            midi_list.append(midi_channels[note])      
        
        


        count_array=[]
            
        for title,scale in diatonic_scale.items():
            count_array.append(library.parser.match_percentage(scale,midi_list))
            pass


        closest_match = max(count_array)


        for title,scale in diatonic_scale.items():

            if int(library.parser.match_percentage(scale,midi_list))==int(closest_match):
                most_common_scale.append(title)
            else:
                pass
            pass

        full_chord_array.extend(most_common_scale)


    pass  


    list_max_array=[] 
    for key,count in library.parser.distinct(full_chord_array).items():

        list_max_array.append(int(count))

        pass

    for key,count in library.parser.distinct(full_chord_array).items():
        if max(list_max_array) == int(count):
            major = key



    return_all_notes=[]

    for midi_note,count in library.parser.distinct(full_list_of_notes_after_max_found).items():
        return_all_notes.append(count)
        pass


 
    for midi_note,count in library.parser.distinct(full_list_of_notes_after_max_found).items():

        if count == max(return_all_notes):

            return controllers.return_key_signature.structure(midi_note)
    
        pass

###########################################################################################################

array=[]
def return_note_array(array):
    note_array=[]
    for note in array:
        note_array.append(library.parser.remove_integers(note))
    return note_array

def match_key_tester(array,item):
    start=0
    overall=0

    for note in return_note_array(item):

        overall=overall+1

        if note in array:
            start = start+1             
    
    return start/overall*100
       
def overall_scale_matcher(total_result):

    percentage_array=[]

    for test in total_result:
        for new in test:
            for scale,percetange in new.items():
                percentage_array.append(percetange)
               
    max_value = max(percentage_array)

    scale_match=[]


    for test in total_result:
        for new in test:
            for scale,percetange in new.items():

                if int(percetange) == int(max_value):
                    scale_match.append(scale)
            
                else:
                    pass

    return library.parser.distinct(scale_match)


def return_key_signature_2(filename):

    array=[]

    total_result=[]

    total_note_count=[]
    
    for item in filename:

        for key,count in item["body"].items():
            total_note_count.append(key)
            
        channel_array=[]
        
        result=[]

        for scale in diatonic_scale:
            result.append({scale:match_key_tester(diatonic_scale[scale],item["body"])})
            channel_array.append({scale:match_key_tester(diatonic_scale[scale],item["body"])})
        pass

        total_result.append(result)

        array.append({
            item["category"]:channel_array
        })

    ##########################################################################################
    number_match=[]

    for scale,number in overall_scale_matcher(total_result).items():
        number_match.extend(number)

    
    return_array=[] 

    for scale,number in overall_scale_matcher(total_result).items():
        

        if max(number_match) in number:

            note_array=[]

            

            for i in range(1,7):

                for note in diatonic_scale[scale]:
                    note_array.append(note+str(i))
                 
            return_array.append({
                scale:note_array
            })
    
    

    return return_array

for filename in library.scan.scan_file_recursively("Z:\\raw_midi\\freemidi\\processed\\json\\*.json"):

    remove_filepath = library.parser.find_and_replace_array(filename,{
        "Z:\\raw_midi\\freemidi\\processed\\json\\":"S:\\Midi-Library\\raw_midi_body_structure\\freemidi\\"
    })

    if library.file.file_exists(filename) and library.json.import_json(filename):

        data = library.json.import_json(filename)
    
        library.json.export_json(remove_filepath,{
            "href":return_key_signature_2(data)
        })

        library.comment.returnMessage("Completed :"+remove_filepath)
    else:
        pass
    

#     remove_filepath = library.parser.find_and_replace_array(filename,{
#         "S:\\Midi-Library\\raw_midi_body_structure\\":"",
#         ".json":""
#     })

#     data = remove_filepath.split("\\")

#     if library.file.file_does_not_exists(app.settings["raw_key_signatures"]+data[0]+"\\"+data[1]+".json"):

#         library.json.export_json(app.settings["raw_key_signatures"]+data[0]+"\\"+data[1]+".json",{
#             "result":return_key_signature_2(filename)
#         })

#         library.comment.returnUpdateMessage("Processing")
    
#     else:
#         pass

# library.comment.returnMessage("Completed   ")

 
