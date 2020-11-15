# import library.parser
# import library.file
import library.json
# import library.midi
import controllers.return_key_signature
#############################################################
# string1="Ace Of Base 2"
# string2="Ace of Base 2"


# count = library.parser.high_match_percentage(string1,string2)
# low = library.parser.low_match_percentage(string1,string2)

##############################################################

# library.file.file_update("S:\\Desktop\\results_3.txt",[
#     "###############",
#     "new line 45",
#     "new line 46",
#     "---",
#     "new line 47"
# ])

##############################################################


array=[]

array.append(controllers.return_key_signature.structure("C"))

library.json.export_json("Z:\\circle_of_fifths.json",array)

