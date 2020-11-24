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

    if percentage_array:
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

def closest_match_handler(total_note_count):
    max_array=[]
    
    for key,value in library.parser.distinct(total_note_count).items():
        max_array.append(int(value))

    max_value=0

    if max_array: max_value = max(max_array)

    scale_return=[]

    for key,value in library.parser.distinct(total_note_count).items():
        if max_value == int(value):
            scale_return.append(key)
    
    return scale_return

def closest_match_handler_dictionary(array):

    return_rating_array=[]

    for item in array:
        for key,value in item.items():
            return_rating_array.append(value)

    max_value=0
    if max(return_rating_array):
        max_value=max(return_rating_array)

    result=[]
    for item in array:
        for key,value in item.items():
            if int(max_value) == int(value):
                    result.append({key:value})
     

    return result


def return_key_signature_2(filename):

    array=[]

    total_result=[]

    total_note_count=[]

    for item in filename:

        if item["category"] !="Drum Kit":
            
            for key,count in item["body"].items():
                 total_note_count.append(library.parser.remove_integers(key))
    
    result=[]
    overall=[]

    for scale in diatonic_scale:
        overall.append(total_note_count)
        result.append({scale:library.parser.match_percentage(diatonic_scale[scale],total_note_count)})


    return{
        "note_list":total_note_count,
        "max":closest_match_handler(total_note_count),
        "matching":result,
        "closest_scale_match":closest_match_handler_dictionary(result)
    } 


for filename in library.scan.scan_file_recursively("Z:\\raw_midi\\freemidi\\processed\\json\\*.json"):

    remove_filepath = library.parser.find_and_replace_array(filename,{
        "Z:\\raw_midi\\freemidi\\processed\\json\\":"S:\\Midi-Library\\raw_midi_body_structure\\freemidi\\"
    })

    if library.file.file_exists(filename) and library.json.import_json(filename):

        library.comment.returnMessage("Processing :"+filename)
    
        data = library.json.import_json(filename)
    
        library.json.export_json(remove_filepath,{
            "href":return_key_signature_2(data)
        })

        library.comment.returnMessage("Completed :"+remove_filepath)
        library.comment.returnMessage("---")
    else:
        pass
