import library.midi
import library.json


midi = library.midi

json = library.json

midi_range=midi.midi_range_array()

return_full_midi_list=[]

return_array_of_notes = midi.return_array_of_notes_from_raw_data("C:\\Users\\Matt\\Desktop\\AllTheSmallThings.json")

print(return_array_of_notes)

# B Minor - Correct key signature
midi.scaleMatchPercentage(return_array_of_notes,['B','C#/Db', 'D', 'E', 'F#/Gb', 'G','A'])

# C Major - incorrect key signature
midi.scaleMatchPercentage(return_array_of_notes,['C','D', 'E', 'F', 'G', 'A','B'])

# D Major - Relative Key
midi.scaleMatchPercentage(return_array_of_notes,['D','E', 'F#/Gb', 'G', 'A', 'B','C#/Db'])


# Scale Intervals - Natural Minor

#Tonic = B (35)


#Natural Minor

minor = midi.scale_generator(35,[2,1,2,2,1,2,2])


#Natural Major

major = midi.scale_generator(26,[2,2,1,2,2,2,1])


# Find the correct or likely match of the natural minor and major key

print("---")


for note in {
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
        "36":"C"
}:

    test_note_name = midi_range[str(note)]

    test_note = note

    minor = midi.scale_generator(int(test_note),[2,1,2,2,1,2,2])

    major = midi.scale_generator(int(test_note),[2,2,1,2,2,2,1])

    print(test_note_name+" minor => "+str(midi.scaleMatchPercentage(return_array_of_notes,minor)))

    print(test_note_name+" major => "+str(midi.scaleMatchPercentage(return_array_of_notes,major)))
 

    
    pass

# We can safely assume that the likely top 80% are going to be the correct scales

for note in {
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
        "36":"C"
}:

    test_note_name = midi_range[str(note)]

    

    test_note = note

    minor = midi.scale_generator(int(test_note),[2,1,2,2,1,2,2])

    major = midi.scale_generator(int(test_note),[2,2,1,2,2,2,1])
    
    if midi.scaleMatchPercentage(return_array_of_notes,minor) > 80:
        test_note_name+" minor => "+str(midi.scaleMatchPercentage(return_array_of_notes,minor))

    if midi.scaleMatchPercentage(return_array_of_notes,major) > 80:
        test_note_name+" major => "+str(midi.scaleMatchPercentage(return_array_of_notes,major))
 
   
    pass

# 80 percentage needs to be learnt by the algorithm - take the high percentage then round it to be nearest decimal - 1st wave 


find_highest_percentage_major=[]
find_highest_percentage_minor=[]

for note in {
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
        "36":"C"
}:

    test_note_name = midi_range[str(note)]

    test_note = note

    minor = midi.scale_generator(int(test_note),[2,1,2,2,1,2,2])

    major = midi.scale_generator(int(test_note),[2,2,1,2,2,2,1])


    find_highest_percentage_minor.append(midi.scaleMatchPercentage(return_array_of_notes,minor))

    find_highest_percentage_major.append(midi.scaleMatchPercentage(return_array_of_notes,major))

  
    pass

max_value_minor = max(find_highest_percentage_minor)

percentage_minor = round(max_value_minor)

max_value_major = max(find_highest_percentage_major)

percentage_major = round(max_value_major)

print("---")
return_array_of_scales=[]

return_array_of_scales_major=[]
return_array_of_scales_minor=[]


for note in {
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
        "36":"C"
}:

    test_note_name = midi_range[str(note)]

    test_note = note

    minor = midi.scale_generator(int(test_note),[2,1,2,2,1,2,2])

    major = midi.scale_generator(int(test_note),[2,2,1,2,2,2,1])

    
    if midi.scaleMatchPercentage(return_array_of_notes,minor) > percentage_minor:

        print(test_note_name+" minor => "+str(midi.scaleMatchPercentage(return_array_of_notes,minor)))

        return_array_of_scales_minor.append(test_note)

    if midi.scaleMatchPercentage(return_array_of_notes,major) > percentage_major:
        print(test_note_name+" major => "+str(midi.scaleMatchPercentage(return_array_of_notes,major)))
        return_array_of_scales_major.append(test_note)
    
    
    pass


json.export_json("C:\\Users\\Matt\\Desktop\\all-the-small-things.json",{
    "artist":"Pink Floyd",
    "song":"Comfortably Numb",
    "major":return_array_of_scales_major,
    "minor":return_array_of_scales_minor,
    "notes":return_full_midi_list
})



# next stage can I teach the algorithm to work out the root note - the system has narrowed down the likelihood of the following being true

# it is either B minor, G major, E minor , D major

# How can a program detect "mood" in a song



import_midi_file =