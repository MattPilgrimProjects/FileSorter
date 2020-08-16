import tb

midi_range={
    "127":"G",
    "126":"F#/Gb",
    "125":"F",
    "124":"E",
    "123":"D#/Eb",
    "122":"D",
    "121":"C#/Db",
    "120":"C",
    "119":"B",
    "118":"A#/Bb",
    "117":"A",
    "116":"G#/Ab",
    "115":"G",
    "114":"F#/Gb",
    "113":"F",
    "112":"E",
    "111":"D#/Eb",
    "110":"D",
    "109":"C#/Db",
    "108":"C",
    "107":"B",
    "106":"A#/Bb",
    "105":"A",
    "104":"G#/Ab",
    "103":"G",
    "102":"F#/Gb",
    "101":"F",
    "100":"E",
    "99":"D#/Eb",
    "98":"D",
    "97":"C#/Db",
    "96":"C",
    "95":"B",
    "94":"A#/Bb",
    "93":"A",
    "92":"G#/Ab",
    "91":"G",
    "90":"F#/Gb",
    "89":"F",
    "88":"E",
    "87":"D#/Eb",
    "86":"D",
    "85":"C#/Db",
    "84":"C",
    "83":"B",
    "82":"A#/Bb",
    "81":"A",
    "80":"G#/Ab",
    "79":"G",
    "78":"F#/Gb",
    "77":"F",
    "76":"E",
    "75":"D#/Eb",
    "74":"D",
    "73":"C#/Db",
    "72":"C",
    "71":"B",
    "70":"A#/Bb",
    "69":"A",
    "68":"G#/Ab",
    "67":"G",
    "66":"F#/Gb",
    "65":"F",
    "64":"E",
    "63":"D#/Eb",
    "62":"D",
    "61":"C#/Db",
    "60":"C",
    "59":"B",
    "58":"A#/Bb",
    "57":"A",
    "56":"G#/Ab",
    "55":"G",
    "54":"F#/Gb",
    "53":"F",
    "52":"E",
    "51":"D#/Eb",
    "50":"D",
    "49":"C#/Db",
    "48":"C",
    "47":"B",
    "46":"A#/Bb",
    "45":"A",
    "44":"G#/Ab",
    "43":"G",
    "42":"F#/Gb",
    "41":"F",
    "40":"E",
    "39":"D#/Eb",
    "38":"D",
    "37":"C#/Db",
    "36":"C",
    "35":"B",
    "34":"A#/Bb",
    "33":"A",
    "32":"G#/Ab",
    "31":"G",
    "30":"F#/Gb",
    "29":"F",
    "28":"E",
    "27":"D#/Eb",
    "26":"D",
    "25":"C#/Db",
    "24":"C"

}

return_array_of_notes=[]

for target_list in tb.import_json("test.json"):
    
    note = target_list.split(":")

    return_array_of_notes.append(midi_range[note[1]])



def scaleMatchPercentage(return_array_of_notes,scale):
    match=0

    for note in return_array_of_notes:

        if note in scale: match = match+1

    
    return str(match)+"/"+str(len(return_array_of_notes))

print(return_array_of_notes)

# B Natural Minor
print(scaleMatchPercentage(return_array_of_notes,['B','C#/Db', 'D', 'E', 'F#/Gb', 'G','A']))

# C Major
print(scaleMatchPercentage(return_array_of_notes,['C','D', 'E', 'F', 'G', 'A','B']))


# D Major - Relative Key
print(scaleMatchPercentage(return_array_of_notes,['D','E', 'F#/Gb', 'G', 'A', 'B','C#/Db']))