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

file_count=0

out = open('api.csv', 'w', newline='', encoding='utf8') 
writer = csv.DictWriter(out, FileInfomation['returnCSVHead'])
writer.writeheader()
for filename in scanFiles["filelist"]:

    file_count = file_count+1

    for column_name in FileInfomation['countColumn']:

        column_title = FileInfomation['returnList'][column_name]
   
        row[column_title]=tb.getDetailsOf(filename,column_name)

    writer.writerow(row)
    tb.returnUpdateMessage(str(file_count) +"/" + str(scanFiles["totalNumberOfFiles"]))

tb.returnMessage("Process complete")