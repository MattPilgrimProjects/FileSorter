
string_1="you-re-a-test"
string_2="you-are-a-test"

def match_percentage(array_1,array_2):

    match=0

    for note in array_1:

        if note in array_2: match = match+1

    return match/len(array_1)*100

print(match_percentage(string_1.split("-"),string_2.split("-")))

