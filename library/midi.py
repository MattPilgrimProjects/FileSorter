import json
import mido
import library.json
import numpy
from scipy import stats
from statistics import mode
import library.parser
import library.maths

notes = ["A","A♯/B♭","B","C","C♯/D♭","D","D♯/E♭","E","F","F♯/G♭","G","G♯/A♭","A","A♯/B♭","B","C","C♯/D♭","D","D♯/E♭","E","F","F♯/G♭","G","G♯/A♭","A","A♯/B♭","B","C"]

note_name_array = library.json.import_json("midi.json")

def import_midi(filename):

    try:
        mid = mido.MidiFile(filename)
    except:
        pass
    else:
        return filename
        # clean(mid)


def time_signature(msg):
    if "time_signature" in msg:
        beat = msg.split("=")[1].split(" ")[0]
        bar = msg.split("=")[2].split(" ")[0]
        return str(beat)+"/"+str(bar)

def key_signature(msg):
    if "key_signature" in msg:
        return msg.split("'")[1]


def bpm(msg):
    array=[]
    if "tempo=" in msg:

        tempo = msg.split("=")[1].replace(" time","")

        note_value = mido.tempo2bpm(int(tempo))
        array.append(note_value)

    return array


def note_list(msg):
    if "note_on" in msg  and "channel=9" not in msg:
        return note_name_array[msg.split("note=")[1].split(" ")[0]]
    # array=[]
    # if "note_on" in msg  and "channel=9" not in msg:
    #     note_value = msg.split("note=")[1].split(" ")[0]
    #     array.append(note_name_array[note_value])
    # return array

def clean(mid):

    mid = mido.MidiFile(mid)

    time_signature_list=[]
    key_signature_list=[]
    note_count_list=[]
    tempo_list=[]

    for i, track in enumerate(mid.tracks):

        for msg in track:

            msg =str(msg)

            if time_signature(msg):
                time_signature_list.append(time_signature(msg))

            if key_signature(msg):
                key_signature_list.append(key_signature(msg))

            if note_list(msg):
                note_count_list.append(note_list(msg))

            if bpm(msg):
                tempo_list.append(bpm(msg))

    
    tempo_list = library.maths.get_mode(tempo_list)
    note_count_list=library.maths.get_distinct(note_count_list)

    single_note_list=[]
    for note in note_count_list:
        single_note_list.append(note)

    major_match = major_list(single_note_list)
    minor_match = minor_list(single_note_list)

    return {
        "midi_time_signature":list(dict.fromkeys(time_signature_list)),
        "tempo":round(tempo_list),
        "note":note_count_list,
        "major_match":major_match,
        "minor_match":minor_match,
        "circle_of_fifths":circle_of_fifths(single_note_list,note_count_list)
    }
    


def cof_handler(note_value,note_count_list):

    try:
        note_count_list[notes[note_value]]
    except:
        major_total=0
    else:
        major_total = note_count_list[notes[note_value]]

    try:
        note_count_list[notes[note_value-3]]
    except:
        minor_total=0
    else:
        minor_total = note_count_list[notes[note_value-3]]
    
    return {
        "Major":notes[note_value],
        "Minor":notes[note_value-3],
        "Total":major_total+minor_total,
        "Major_Count":major_total,
        "Minor_Count":minor_total

    }


def circle_of_fifths(note_list,note_count_list):

  

    circle_segment=[
            cof_handler(3,note_count_list),
            cof_handler(10,note_count_list),
            cof_handler(5,note_count_list),
            cof_handler(12,note_count_list),
            cof_handler(7,note_count_list),
            cof_handler(14,note_count_list),
            cof_handler(9,note_count_list),
            cof_handler(4,note_count_list),
            cof_handler(11,note_count_list),
            cof_handler(6,note_count_list),
            cof_handler(13,note_count_list),
            cof_handler(8,note_count_list)
         
    ]

    export_list =[]

    for note in note_list:

        if "\u266f" in note:
            export_list.append(1)
        else:
            pass
        
    if len(export_list)==0:
        return (
            circle_segment[0]
        )
     
    
    if len(export_list)==1:
        major=circle_segment[1]
    
    if len(export_list)==2:
        return (
            circle_segment[2],
            circle_segment[3],
            circle_segment[11],
            circle_segment[10]
        )

    if len(export_list)==3:
        return(
            circle_segment[3],
            circle_segment[4],
            circle_segment[9],
            circle_segment[8]
        )

    if len(export_list)==4:
        return(
             circle_segment[4],
             circle_segment[5],
             circle_segment[8],
             circle_segment[7]
        )

    if len(export_list)==5:
        return(
            circle_segment[5],
            circle_segment[6],
            circle_segment[7]

        )
        
     

   
    
 
   

def return_max_value(note_list):
    count_list=[]
    for note,count in note_list.items():
        count_list.append(count)
   
    max_value = max(count_list)
    return_closet_match =[]
    for note,count in note_list.items():

        if count == max_value:
            return_closet_match.append(note)
   
    return return_closet_match

def predictor(note_list,major,minor,first_set_of_notes):

    mode_scale=[]

    for note in  library.maths.get_distinct(first_set_of_notes):

        if major[note] >= minor[note]:
            mode_scale.append(note+" Major")
         
        else:
            mode_scale.append(note+" Minor")

    return mode_scale

def scale_match(check,scale):

    matched=0

    for note in check:
        if note in scale:
            matched = matched + 1

    return matched/len(scale)*100

def minor_list(single_note_list):
    export_list =[]

    for note in range(3,15):
        export_list.append((notes[note],minor_scale(notes[note],single_note_list)))

    return library.parser.convert_tuples_to_dictionary(export_list)

def major_list(single_note_list):

    export_list =[]

    for note in range(3,15):
        export_list.append((notes[note],major_scale(notes[note],single_note_list)))

    return library.parser.convert_tuples_to_dictionary(export_list)

def major_scale(root_note,check):
    root_value = notes.index(root_note)
    result_export=[]
    for i in [0,2,4,5,7,9,11]:
        result_export.append(notes[i+root_value])
    return scale_match(check,result_export)

def minor_scale(root_note,check):
    root_value = notes.index(root_note)
    result_export=[]
    for i in [0,2,3,5,7,8,10]:
        result_export.append(notes[i+root_value])
    
    return scale_match(check,result_export)