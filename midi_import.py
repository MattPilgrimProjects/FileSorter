from mido import MidiFile
import library.tb
mid = MidiFile('C:\\Users\\Matt\\Desktop\\test.mid')

tb = library.tb

row={}
test=[]
array=[]

channel=""
note_value=""

returnValue={}

for i, track in enumerate(mid.tracks):
    
    for msg in track:

        msg = str(msg)

        msg = msg.split(" ")

        for tag in msg:

            if "channel" in tag:
                channel = tag.replace("channel=","")
              

            if "note" in tag and "note_on" not in tag and "note_off" not in tag and "notes" not in tag:
                note_value = tag.replace("note=","")

                array.append(str(channel+":"+note_value))

array = tb.removeDuplicates(array)
tb.export_json("C:\\Users\\Matt\\Desktop\\test.json",array)

          
        
             

     
