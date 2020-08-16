from mido import MidiFile
import tb
mid = MidiFile('test.mid')

row={}
test=[]

for i, track in enumerate(mid.tracks):
    
    for msg in track:

        if "note_on" in str(msg):

            array = str(msg).split(" ")

            data={}
            data_fixed={}

            for key in array:
                
                row=key.split("=")

                if len(row) ==2:

                    data[row[0]]=row[1]

                    for key1,value1 in data.items():

                        if "velocity" not in key1 and "time" not in key1:

                            data_fixed[key1]=value1

                    test.append(data_fixed)
       
tb.export_json("test.json",test)