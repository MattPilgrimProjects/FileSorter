import app
import library

full_array=[]

for filename in library.scan.scan_file_recursively("S:\\Midi-Library\\raw_keywords\\csv\\*\\*.csv"):

    for csv_row in library.csv.importCSVData(filename):
        full_array.append(csv_row[0])

    pass

csv_array_return=[]
for key in library.parser.remove_duplicates_from_array(full_array):

    csv_array_return.append({"href":key})

library.csv.export_csv("merge_all_keywords.csv",["href"],csv_array_return)
library.file.execute("merge_all_keywords.csv")