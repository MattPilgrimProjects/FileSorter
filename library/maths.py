from statistics import mode
import library.parser

# This library is calculations primarily for machine learning
def list_constructor(lst):
    list_return=[]
    for item in lst:
        list_return.append(item[0])
    return list_return

def get_mode(lst):
    lst = list_constructor(lst)
    return mode(lst)

def get_mode_list(lst):
    return mode(lst)

def get_max(lst):
    return max(lst)


def get_distinct(lst):
    export_list=[]
    for note in list(dict.fromkeys(lst)):
        export_list.append((note,lst.count(note)))

    return library.parser.convert_tuples_to_dictionary(export_list)