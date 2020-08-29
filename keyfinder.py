import library.midi
import library.json
import library.scan
import library.tb



setup = library.json.import_json("setup.json")

notes_sample_size={
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
}


midi = library.midi

json = library.json

midi_range=midi.midi_range_array()

return_full_midi_list=[]



for filename in library.scan.scanFilesRecursively("C:\\inetpub\\wwwroot\\api\\live\\library\\**\\*.json"):

    try:
        library.json.import_json(filename)['midi']
    except KeyError:
        library.tb.returnMessage("MIDI not found")
    else:

        return_array_of_notes = midi.return_array_of_notes_from_raw_data(filename)

        # Find the correct or likely match of the natural minor and major key

        find_highest_percentage_major=[]
        find_highest_percentage_minor=[]

        for note in notes_sample_size:

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


        for note in notes_sample_size:

            test_note_name = midi_range[str(note)]

            test_note = note

            minor = midi.scale_generator(int(test_note),[2,1,2,2,1,2,2])

            major = midi.scale_generator(int(test_note),[2,2,1,2,2,2,1])

            
            if midi.scaleMatchPercentage(return_array_of_notes,minor) > percentage_minor:

                #print(test_note_name+" minor => "+str(midi.scaleMatchPercentage(return_array_of_notes,minor)))

                return_array_of_scales_minor.append(test_note_name+" Minor")

            if midi.scaleMatchPercentage(return_array_of_notes,major) > percentage_major:
                #print(test_note_name+" major => "+str(midi.scaleMatchPercentage(return_array_of_notes,major)))
                return_array_of_scales_minor.append(test_note_name+" Major")
            
            
            pass


        json.update_json(filename,{
            "scale_notes":library.tb.removeDuplicates(return_array_of_notes),
            "scale_match":return_array_of_scales_minor
        })

        library.tb.returnMessage("Updated =>"+filename)

pass

