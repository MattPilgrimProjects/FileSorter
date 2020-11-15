import library.json

def remove_int(ini_string):
    return ''.join([i for i in ini_string if not i.isdigit()])

def ui(scale):

    return_array=[]

    for note in library.json.import_json("midi_notes.json"):

        if remove_int(note) in scale:
            return_array.append(note)
    
    return return_array

def structure(note):

    note_to_int_value={
        "C":12,
        "C#/Db":13,
        "D":14,
        "D#/Eb":15,
        "E":16,
        "F":17,
        "F#/Gb":18,
        "G":19,
        "G#/Ab":20,
        "A":21,
        "A#/Bb":22,
        "B":23
    }

    note_value=note_to_int_value[note]

    keyboard=[
    "C","C#/Db","D","D#/Eb","E","F","F#/Gb","G","G#/Ab","A","A#/Bb","B",
    "C","C#/Db","D","D#/Eb","E","F","F#/Gb","G","G#/Ab","A","A#/Bb","B",
    "C","C#/Db","D","D#/Eb","E","F","F#/Gb","G","G#/Ab","A","A#/Bb","B"
    ]

    


    # Major Structure =[0,2,4,5,7,9,11,12]
    # Music Theory =[R,T,T,S,T,T,T,S]
    scale=note_value
    major_structure=[0+scale,2+scale,4+scale,5+scale,7+scale,9+scale,11+scale]

    scale=note_value-3
    relative_key=[0+scale,2+scale,3+scale,5+scale,7+scale,8+scale,10+scale]

    major=[]
    relative=[]


    for note in range(len(keyboard)):


        if note in major_structure: major.append(keyboard[note])

        if note in relative_key: relative.append(keyboard[note])


    major_array=[]
    minor_array=[]
    
    min_value=1

    

    for i in range(min_value,10):

        for major_note in major:
            major_array.append(major_note+str(i))
        for minor_note in relative:
            minor_array.append(minor_note+str(i))
           
            
   

    return {
        "major_root_note":major[0] +" Major",
        "minor_root_note":relative[0]+" Minor",
        "major":major_array,
        "relative":minor_array
    }