import library.tb
import library.csv
import library.comment

tb = library.tb
csv = library.csv

library.comment.returnMessage("Scanning drives")

scanFiles=tb.scanFilesRecursively()

if scanFiles["totalNumberOfFiles"]==0:
    library.comment.returnMessage("No data found")
    quit()
else:
    library.comment.returnMessage(str(scanFiles["totalNumberOfFiles"])+" files found")
    library.comment.returnMessage("Exporting data")

row={}
 
FileInfomation = tb.returnFileInformation()

file_count=0

writer = csv.create_csv_header("api.csv",FileInfomation['returnCSVHead'])

for filename in scanFiles["filelist"]:

    file_count = file_count+1

    for column_name in FileInfomation['countColumn']:

        column_title = FileInfomation['returnList'][column_name]
   
        row[column_title]=tb.getDetailsOf(filename,column_name)

    writer.writerow(row)
    
    library.comment.returnUpdateMessage(str(file_count) +"/" + str(scanFiles["totalNumberOfFiles"]))

library.comment.returnMessage("Process complete")