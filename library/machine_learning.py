import library.parser
import library.comment

def check_value_against_list(data,artist_list):

    artist_match_list = []

    for check_artist in artist_list:

        high = library.parser.high_match_percentage(check_artist, data)

        if high >= 80.0:
            artist_match_list.append((check_artist, high))

   
    return library.parser.convert_tuples_to_dictionary(artist_match_list)


def match_by_percentage(value_1,value_2):
    return library.parser.high_match_percentage(value_1, value_2)