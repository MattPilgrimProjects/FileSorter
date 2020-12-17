# import library.parser
# import library.file
import library.json
import library.midi
import controllers.return_key_signature
import library.parser
import library.file
# #############################################################
# # string1="Ace Of Base 2"
# # string2="Ace of Base 2"


# # count = library.parser.high_match_percentage(string1,string2)
# # low = library.parser.low_match_percentage(string1,string2)

# ##############################################################

# # library.file.file_update("S:\\Desktop\\results_3.txt",[
# #     "###############",
# #     "new line 45",
# #     "new line 46",
# #     "---",
# #     "new line 47"
# # ])

# ##############################################################


# array=[]

# array.append(controllers.return_key_signature.structure("C"))

# ##############################################################


# dictionary=[
#     {
#         "test":"hello",
#         "hello":"yo"
#     },
#     {
#         "test":"test2"
#     },
#     {
#         "test":"hello",
#         "hello":"yo"
#     }
# ]

# # print(library.parser.remove_duplicates_from_dictionary(dictionary))



# dictionary_2=[
#     {
#         "artist": "King Fish Man",
#         "album": "Hey Big Fishy!",
#         "album_artwork": "https://i.scdn.co/image/ab67616d0000b2734b1d17ebf282302d754c5daa",

#     },
#     {
#         "artist": "10,000 Maniacs",
#         "album": "MTV Unplugged",
#         "album_artwork": "https://i.scdn.co/image/ab67616d0000b273c2b347ff549319d8cdd96e31",

#     },
#     {
#         "artist": "10,000 Maniacs",
#         "album": "In My Tribe",
#         "album_artwork": "https://i.scdn.co/image/ab67616d0000b2736b90e1c1b6991129a2769222",
#     },
#     {
#         "artist": "10,000 Maniacs",
#         "album": "Original Album Series",
#         "album_artwork": "https://i.scdn.co/image/ab67616d0000b273b813665459f40bf86a8b31af",
#     },
#     {
#         "artist": "10,000 Maniacs",
#         "album": "In My Tribe",
#         "album_artwork": "https://i.scdn.co/image/ab67616d0000b27367256c7d4378b5d6f9c125bc",
#     }
# ]

# test  = library.parser.compress_dictionary(dictionary_2)

# txt = "Céline Dion"

# x = txt.encode(encoding="ascii",errors="namereplace")


# content = library.midi.import_midi("S:\\Downloads\\lights.mid")
# library.json.export_json("test.json",content)
# library.file.execute("test.json")
# filename = "africa"
# library.midi.import_midi("S:\\Downloads\\"+filename+".mid","S:\\Downloads\\"+filename+".json")
# library.file.execute("S:\\Downloads\\"+filename+".json")
# high = library.parser.high_match_percentage("AC/DC","ac-dc")
# print(high)
from mido import MidiFile

mid = MidiFile('S:\\Midi-Library\\mididb\\midi\\depeche-mode-enjoy-the-silence.mid')

for i, track in enumerate(mid.tracks):
    
    for msg in track:
        msg=str(msg)

        if "channel=1 " in msg and "note" in msg:
            print(msg)
        else:
            pass