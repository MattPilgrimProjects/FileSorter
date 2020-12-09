import json
import mido
import library.json
import numpy
from scipy import stats

notes = ["A","A♯/B♭","B","C","C♯/D♭","D","D♯/E♭","E","F","F♯/G♭","G","G♯/A♭","A","A♯/B♭","B","C","C♯/D♭","D","D♯/E♭","E","F","F♯/G♭","G","G♯/A♭","A","A♯/B♭","B","C"]

def midi_range_array_by_note():
    return{
            "C":"0",
            "C#/Db":"1",
            "D":"2",
            "D#/Eb":"3",
            "E":"4",
            "F":"5",
            "F#/Gb":"6",
            "G":"7",
            "G#/Ab":"8",
            "A":"9",
            "A#/Bb":"10",
            "B":"11",
            "C":"12",
            "C#/Db":"13",
            "D":"14",
            "D#/Eb":"15",
            "E":"16",
            "F":"17",
            "F#/Gb":"18",
            "G":"19",
            "G#/Ab":"20",
            "A":"21",
            "A#/Bb":"22",
            "B":"23",
            "C":"24",
            "C#/Db":"25",
            "D":"26",
            "D#/Eb":"27",
            "E":"28",
            "F":"29",
            "F#/Gb":"30",
            "G":"31",
            "G#/Ab":"32",
            "A":"33",
            "A#/Bb":"34",
            "B":"35",
            "C":"36",
            "C#/Db":"37",
            "D":"38",
            "D#/Eb":"39",
            "E":"40",
            "F":"41",
            "F#/Gb":"42",
            "G":"43",
            "G#/Ab":"44",
            "A":"45",
            "A#/Bb":"46",
            "B":"47",
            "C":"48",
            "C#/Db":"49",
            "D":"50",
            "D#/Eb":"51",
            "E":"52",
            "F":"53",
            "F#/Gb":"54",
            "G":"55",
            "G#/Ab":"56",
            "A":"57",
            "A#/Bb":"58",
            "B":"59",
            "C":"60",
            "C#/Db":"61",
            "D":"62",
            "D#/Eb":"63",
            "E":"64",
            "F":"65",
            "F#/Gb":"66",
            "G":"67",
            "G#/Ab":"68",
            "A":"69",
            "A#/Bb":"70",
            "B":"71",
            "C":"72",
            "C#/Db":"73",
            "D":"74",
            "D#/Eb":"75",
            "E":"76",
            "F":"77",
            "F#/Gb":"78",
            "G":"79",
            "G#/Ab":"80",
            "A":"81",
            "A#/Bb":"82",
            "B":"83",
            "C":"84",
            "C#/Db":"85",
            "D":"86",
            "D#/Eb":"87",
            "E":"88",
            "F":"89",
            "F#/Gb":"90",
            "G":"91",
            "G#/Ab":"92",
            "A":"93",
            "A#/Bb":"94",
            "B":"95",
            "C":"96",
            "C#/Db":"97",
            "D":"98",
            "D#/Eb":"99",
            "E":"100",
            "F":"101",
            "F#/Gb":"102",
            "G":"103",
            "G#/Ab":"104",
            "A":"105",
            "A#/Bb":"106",
            "B":"107",
            "C":"108",
            "C#/Db":"109",
            "D":"110",
            "D#/Eb":"111",
            "E":"112",
            "F":"113",
            "F#/Gb":"114",
            "G":"115",
            "G#/Ab":"116",
            "A":"117",
            "A#/Bb":"118",
            "B":"119",
            "C":"120",
            "C#/Db":"121",
            "D":"122",
            "D#/Eb":"123",
            "E":"124",
            "F":"125",
            "F#/Gb":"126"
    }

def midi_range_array():
    return {
        "0":"C",
        "1":"C#/Db",
        "2":"D",
        "3":"D#/Eb",
        "4":"E",
        "5":"F",
        "6":"F#/Gb",
        "7":"G",
        "8":"G#/Ab",
        "9":"A",
        "10":"A#/Bb",
        "11":"B",
        "12":"C",
        "13":"C#/Db",
        "14":"D",
        "15":"D#/Eb",
        "16":"E",
        "17":"F",
        "18":"F#/Gb",
        "19":"G",
        "20":"G#/Ab",
        "21":"A",
        "22":"A#/Bb",
        "23":"B",
        "24":"C",
        "25":"C#/Db",
        "26":"D",
        "27":"D#/Eb",
        "28":"E",
        "29":"F",
        "30":"F#/Gb",
        "31":"G",
        "32":"G#/Ab",
        "33":"A",
        "34":"A#/Bb",
        "35":"B",
        "36":"C",
        "37":"C#/Db",
        "38":"D",
        "39":"D#/Eb",
        "40":"E",
        "41":"F",
        "42":"F#/Gb",
        "43":"G",
        "44":"G#/Ab",
        "45":"A",
        "46":"A#/Bb",
        "47":"B",
        "48":"C",
        "49":"C#/Db",
        "50":"D",
        "51":"D#/Eb",
        "52":"E",
        "53":"F",
        "54":"F#/Gb",
        "55":"G",
        "56":"G#/Ab",
        "57":"A",
        "58":"A#/Bb",
        "59":"B",
        "60":"C",
        "61":"C#/Db",
        "62":"D",
        "63":"D#/Eb",
        "64":"E",
        "65":"F",
        "66":"F#/Gb",
        "67":"G",
        "68":"G#/Ab",
        "69":"A",
        "70":"A#/Bb",
        "71":"B",
        "72":"C",
        "73":"C#/Db",
        "74":"D",
        "75":"D#/Eb",
        "76":"E",
        "77":"F",
        "78":"F#/Gb",
        "79":"G",
        "80":"G#/Ab",
        "81":"A",
        "82":"A#/Bb",
        "83":"B",
        "84":"C",
        "85":"C#/Db",
        "86":"D",
        "87":"D#/Eb",
        "88":"E",
        "89":"F",
        "90":"F#/Gb",
        "91":"G",
        "92":"G#/Ab",
        "93":"A",
        "94":"A#/Bb",
        "95":"B",
        "96":"C",
        "97":"C#/Db",
        "98":"D",
        "99":"D#/Eb",
        "100":"E",
        "101":"F",
        "102":"F#/Gb",
        "103":"G",
        "104":"G#/Ab",
        "105":"A",
        "106":"A#/Bb",
        "107":"B",
        "108":"C",
        "109":"C#/Db",
        "110":"D",
        "111":"D#/Eb",
        "112":"E",
        "113":"F",
        "114":"F#/Gb",
        "115":"G",
        "116":"G#/Ab",
        "117":"A",
        "118":"A#/Bb",
        "119":"B",
        "120":"C",
        "121":"C#/Db",
        "122":"D",
        "123":"D#/Eb",
        "124":"E",
        "125":"F",
        "126":"F#/Gb",

    }

def scaleMatchPercentage(return_array_of_notes,scale):

    if scale==None:
        print("No Notes")
    else:
    
        match=0

        for note in return_array_of_notes:

            if note in scale: match = match+1

    return match/len(return_array_of_notes)*100

def scale_generator(tonic,intervals):
    interval = tonic
    x=0  
    scale_array = [] 

    midi_range = midi_range_array()

    if tonic < 120:

        for key in intervals:

            x=x+1

            interval = interval+key

            scale_array.append(midi_range[str(interval)])

        return scale_array

def return_array_of_notes_from_raw_data(filename):

    return_array_of_notes=[]
    channel_array=[]

    midi_range = midi_range_array()

    try:
        import_json(filename)['midi']
    except KeyError:
        pass
    else:
    
        for note in import_json(filename)['note_sequence']:

            return_array_of_notes.append(midi_range[note]) 

    return return_array_of_notes

def removeDuplicates(array):
    return list(dict.fromkeys(array))

def import_json(filename):
    jsonFile = open(filename, 'r')
    config = json.load(jsonFile)
    jsonFile.close()
    return config


      
def midi_output(mid):

    array=[]
    
    for i, track in enumerate(mid.tracks):

        for msg in track:

            msg = str(msg)

            msg = msg.split(" ")

            for tag in msg:

                if "channel" in tag:
                    channel = tag.replace("channel=","")
                        

                if "note" in tag and "note_on" not in tag and "note_off" not in tag and "notes" not in tag:
                    note_value = tag.replace("note=","")
                    array.append(note_value)
              
    return array


def export_processed_content(mid,process_filename):
    
    array=[]
    
    for i, track in enumerate(mid.tracks):

        for msg in track:

            msg = str(msg)

            array.append(msg)

    

    return array


def read_midi(filename):

    channel_name  = library.json.import_json("S:\\Midi-Library\\instruments.json")
    instrumental_type = library.json.import_json("S:\\Midi-Library\\instruments_types.json")

    array=[]
    mid = mido.MidiFile(filename)

    midi_channels = library.json.import_json("P:\\midi.json")

    for i, track in enumerate(mid.tracks):
        
        channel = track.name

        note_array=[]

        raw_msg=""

        raw_data=[]
        

        for msg in track:
            
            msg = str(msg)
             
            # if "note_on " in msg:
            #     note_array.append(midi_channels[msg.split("note=")[1].split(" ")[0]])

            # if "program_change" in msg:
            #     raw_msg = msg.split("program=")[1].split(" ")[0]
  
            # raw_data.append(msg)
         
            # if "channel=9" in msg:
            #     raw_msg="Dr"

            array.append(msg)

        # if note_array:        
        #     array.append({
        #             "channel":channel,
        #             "body":library.parser.distinct(note_array),
        #             "category":instrumental_type[channel_name[raw_msg]],
        #             "instrument":channel_name[raw_msg],
                    
        # #         })
        # else:
        #     pass
    return array
  

def return_notes_and_channels(midi_filename):

    try:
        mid = read_midi(midi_filename)
    except Exception as e:
        print("File Error " + midi_filename+ ":"+str(e))   
        return None

    else:
        return mid


def import_midi(filename):

    # return mido.tempo2bpm(703914)

    

    mid = mido.MidiFile(filename)
    
    array=[]

    raw=[]

    time_signature=""

    meta=[]
    notes=[]
    note_dump=[]

    note_name = library.json.import_json("midi.json")

    for i, track in enumerate(mid.tracks):

      
        for msg in track:         
            
            msg = str(msg)

            raw.append(msg)
    

            if "tempo=" in msg:

                tempo = msg.split("=")[1].replace(" time","")

                array.append(mido.tempo2bpm(int(tempo)))

            if "time_signature" in msg:

                beat = msg.split("=")[1].split(" ")[0]
                bar = msg.split("=")[2].split(" ")[0]

                time_signature= beat+"/"+bar


            if "note_on" in msg:

                if "channel=9" in msg:
                    pass
                else:

                    note = msg.split("=")[2].split(" ")[0]

                    note_dump.append(note_name[note])
           
                    notes.append(note)

    note_match_array=[]    
    most_notes=[]
    for key,value in library.parser.distinct(notes).items():

        note_match_array.append(note_name[key])
        most_notes.append({note_name[key]:value})

    

    major_scale_match=scale_handler(note_match_array,[1,3,4,6,8,10])
    minor_scale_match = scale_handler(note_match_array,[1, 2, 4, 6,7,9])
    closest_match = library.parser.distinct(note_match_array)
    note_dump_results = library.parser.distinct(note_dump)
    key_detection = smart_match_major(return_max(minor_scale_match),return_max(major_scale_match),closest_match)
    key_signature = mode(closest_match,note_dump_results,key_detection)
    if key_signature==None:
        print("second filter")
        key_detection=ambigious_data_filter(return_max(minor_scale_match),return_max(major_scale_match))
        key_signature = mode(closest_match,note_dump_results,key_detection)


    return {
        "bpm": str(round(numpy.median(array))),
        "time_signature":time_signature,
        "note_dump":note_dump_results,
        "closest_match":closest_match,
        "dev":{
            "major_scale":major_scale_match,
            "minor_scale":minor_scale_match,
            "reduced_minor_match":return_max(minor_scale_match),
            "reduced_major_match":return_max(major_scale_match)
        },
        "key_detection":key_detection,
        "key_signature":key_signature
    
        
    }
def get_relative_major(note):
    major_note__index_position= notes.index(note)

    return notes[major_note__index_position+3]

def get_relative_minor(note):
    major_note__index_position= notes.index(note)

    return notes[major_note__index_position-3]

def ambigious_data_filter(minor_list,major_list):

    return_major=[]
    return_minor=[]

    for note in major_list:

        if get_relative_minor(note) in minor_list:
            return_major.append((note+" Major",get_relative_minor(note)+" Minor"))
        
    for minor_note in minor_list:

        if get_relative_minor(minor_note) in major_list:
            return_minor.append((minor_note+" Minor",get_relative_major(minor_note)+" Major"))

            
    if len(return_minor)==1:
        return {
            "major":return_minor[0][1],
            "minor":return_minor[0][0]
        }
    
    if len(return_major)==1:
        return {
            "major":return_major[0][0],
            "minor":return_major[0][1]
        }
    


    

def mode(mode,note_dump_results,key_detection):

    note_deviation_filter=[]
    note_deviation_filter_2=[]

    for note_dump,note_dump_count in note_dump_results.items():
        if note_dump in key_detection["major"] or note_dump in key_detection["minor"]:
            note_deviation_filter.append((note_dump,note_dump_count))
    


    for mode_note,mode_note_count in mode.items():
        if mode_note in key_detection["major"] or mode_note in key_detection["minor"]:
            note_deviation_filter_2.append((mode_note,mode_note_count))
    
    if note_deviation_filter and note_deviation_filter_2:
        list_1 = return_max(library.parser.convert_tuples_to_dictionary(note_deviation_filter))
        list_2 = return_max(library.parser.convert_tuples_to_dictionary(note_deviation_filter_2))
        list_3 = list_1+list_2
        final_note = return_max(library.parser.distinct(list_3))
  
        for note in final_note:

            
            if note in key_detection["major"]:
                return note + " Major"
            if note in key_detection["minor"]:
                return note + " Minor"

def smart_match_major(minor,major,calculations):

    overal=[]

    minor_highest_list=[]
    major_highest_list=[]

    for note,count in calculations.items():

        for minor_note in minor:
            if minor_note == note:
                minor_highest_list.append((note,count))
        

        for major_note in major:
            if major_note == note:
                major_highest_list.append((note,count))
    
    # check major against relative minor

    notes = ["A","A♯/B♭","B","C","C♯/D♭","D","D♯/E♭","E","F","F♯/G♭","G","G♯/A♭","A","A♯/B♭","B","C","C♯/D♭","D","D♯/E♭","E","F","F♯/G♭","G","G♯/A♭","A","A♯/B♭","B","C"]

    minor_max = dict((x, y) for x, y in minor_highest_list)
    major_max = dict((x, y) for x, y in major_highest_list)


         
    return{
        "major":find_relative_major(minor_max,major_max),
        "minor":find_relative_minor(minor_max,major_max),
    }

notes = ["A","A♯/B♭","B","C","C♯/D♭","D","D♯/E♭","E","F","F♯/G♭","G","G♯/A♭","A","A♯/B♭","B","C","C♯/D♭","D","D♯/E♭","E","F","F♯/G♭","G","G♯/A♭","A","A♯/B♭","B","C"]

def find_relative_major(major_max,minor_max):

    check_for_relative_major = []
    return_minor=[]

    for note in return_max(major_max):

        

        if get_relative_major(note) in minor_max:
            check_for_relative_major.append(get_relative_major(note))
        
    
    if len(check_for_relative_major):
        return_minor = check_for_relative_major[0]

    return return_minor

     
def find_relative_minor(minor_max,major_max):
    

    check_for_relative_major = []
    return_minor=[]

    for note in return_max(minor_max):
        minor_note__index_position = notes.index(note)



        if notes[minor_note__index_position+3] in major_max:
            check_for_relative_major.append(note)
        

    if len(check_for_relative_major):
        return_minor = check_for_relative_major[0]
    
    return return_minor


def return_max(array):

    count_array=[]

    for note,count in array.items():
        count_array.append(count)

    max_value=max(count_array)

    return_array=[]

    for note_2,count_2 in array.items():

        if max_value==count_2:
            return_array.append(note_2)
    
    return return_array



def scale_handler(note_dump,intervals):

    return_array=[]

    for return_note in library.parser.distinct(note_dump):

        return_array.append(return_note)

    return {
        "C":output_handler("C",return_array,intervals),
        
        "C♯/D♭":output_handler("C♯/D♭",return_array,intervals),

        "D":output_handler("D",return_array,intervals),

        "D♯/E♭":output_handler("D♯/E♭",return_array,intervals),

        "E":output_handler("E",return_array,intervals),

        "F":output_handler("F",return_array,intervals),

        "F♯/G♭":output_handler("F♯/G♭",return_array,intervals),

        "G":output_handler("G",return_array,intervals),

        "G♯/A♭":output_handler("G♯/A♭",return_array,intervals),

        "A":output_handler("A",return_array,intervals),

        "A♯/B♭":output_handler("A♯/B♭",return_array,intervals),

        "B":output_handler("B",return_array,intervals)
    }

def output_handler(note,return_array,intervals):
    return library.parser.match_percentage(minor_scale(note,intervals),return_array)
    
def major_scale(root_note):

    notes = ["A","A♯/B♭","B","C","C♯/D♭","D","D♯/E♭","E","F","F♯/G♭","G","G♯/A♭","A","A♯/B♭","B","C","C♯/D♭","D","D♯/E♭","E","F","F♯/G♭","G","G♯/A♭","A","A♯/B♭","B","C"]

    i=0
    for note in notes:

        i=i+1

        if root_note==note: root_note=i
 
    major_scale_array = [0, 2, 4, 5,7,9,11]

    array = []

    for sequence in major_scale_array:
        array.append(notes[root_note+sequence])

    return array


def minor_scale(root_note,scale):

    original_note = root_note

    notes = ["A","A♯/B♭","B","C","C♯/D♭","D","D♯/E♭","E","F","F♯/G♭","G","G♯/A♭","A","A♯/B♭","B","C","C♯/D♭","D","D♯/E♭","E","F","F♯/G♭","G","G♯/A♭","A","A♯/B♭","B","C"]

    i=0
    for note in notes:

        i=i+1

        if root_note==note: root_note=i
 
    major_scale_array = scale

    array = []

    array.append(original_note)
    for sequence in major_scale_array:
        array.append(notes[root_note+sequence])

    return array



