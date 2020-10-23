import app
import library


def return_key_signature(filename):

    library.comment.returnMessage("Processing:"+filename)

    file_content = library.json.import_json(filename)

    midi_channels = library.json.import_json("midi.json")

    diatonic_scale={
        "C Major":["C","D","E","F","G","A","B"],
        "D Major":["D", "E","F#/Gb", "G","A", "B", "C#/Db"],
        "E Major":["E", "F#/Gb", "G#/Ab", "A", "B", "C#/Db", "D#/Eb"],
        "F Major":["F","G","A","A#/Bb","C","D","E"],
        "G Major":["G","A","B","C","D","E","F#/Gb"],
        "A Major":["A","B","C#/Db","D","E","F#/Gb","G#/Ab"],
        "B Major":["B", "C#/Db", "D#/Eb", "E", "F#/Gb", "G#/Ab", "A#/Bb"]
    }

    minor_scales={
        "B Minor":["B","C#/Db","D", "E","F#/Gb", "G","A"]
    }

    full_chord_array=[]
    full_notes_list=[]
    return_all_notes=[]
    full_list_of_notes_after_max_found=[]

    for channel,note_array in file_content.items():

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


    return_all_notes_result=[]

    for midi_note,count in library.parser.distinct(full_list_of_notes_after_max_found).items():

        if count == max(return_all_notes):

    

            if midi_note in major:
                return major
                # print(diatonic_scale[major])
            else:
                return midi_note+" Minor"
                # print(minor_scales[midi_note+" Minor"])
                
                pass

    

        pass



array=[]

for filename in library.scan.scan_file_recursively("S:\\Midi-Library\\raw_midi_body_structure\\*\\*.json"):

    remove_filepath = library.parser.find_and_replace_array(filename,{
        "S:\\Midi-Library\\raw_midi_body_structure\\":"",
        ".json":""
    })

    data = remove_filepath.split("\\")

    array.append({
        "source":data[0],
        "id":data[1],
        "result":return_key_signature(filename)
    })

library.json.export_json("S:\\Midi-Library\\sources\\key_signature_list.json",array)

 
