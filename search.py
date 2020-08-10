import tb
import os
import csv

tb.returnMessage("Scanning drives")

scanFiles=tb.scanFilesRecursively()

if scanFiles["totalNumberOfFiles"]==0:
    tb.returnMessage("No data found")
    quit()

tb.returnMessage(str(scanFiles["totalNumberOfFiles"])+" files found")
tb.returnMessage("Exporting data")


row={}

FileInfomation = tb.returnFileInformation()

print(FileInfomation)

# out = open('api.csv', 'w', newline='', encoding='utf8') 
# writer = csv.DictWriter(out, FileInfomation['returnCSVHead'])
# writer.writeheader()
for filename in scanFiles["filelist"]:

    print(FileInformation["returnCSVHead"])

#     a = a+1

#     for column_name in FileInformation["returnCSVHead"]:

#         row[FileInformation[returnList[column_name]]]=tb.getDetailsOf(filename,column_name)

#     writer.writerow(row)
#     tb.returnMessage(str(a) +"/" + str(scanFiles[totalNumberOfFiles]))
#     #print(tb.get_current_date()+" => " + str(a) +"/" + str(i),end="\r")

#     pass

# tb.returnMessage("Process complete")


