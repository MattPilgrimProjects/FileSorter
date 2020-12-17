sources = ["mididb","midiworld","freemidi"]
data_export=[]
for source in sources:
    data_export.append({
        "directory":{
            "S:\\Midi-Library\\"+source+"\\",
            "S:\\Midi-Library\\"+source+"\\midi\\",
            "S:\\Midi-Library\\"+source+"\\midi-library\\"
            },
        
        "file":{    
            "S:\\Midi-Library\\"+source+"\\midi-library.json",
            "S:\\Midi-Library\\"+source+"\\check.json"
        }
    })

