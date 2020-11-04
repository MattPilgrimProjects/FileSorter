import csv

def create_csv_header(filename,csv_header):
    out = open(filename, 'w', newline='', encoding='utf-8') 
    writer = csv.DictWriter(out, csv_header)
    writer.writeheader()
    return writer


def createCSVHeader(filepath, header):
    out = open(filepath, 'w', newline='', encoding='utf-8') 
    writer = csv.DictWriter(out,header)
    writer.writeheader()
    return writer

def importCSVData(filename):
    returnFile=[]
    with open(filename, encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            returnFile.append(row) 
        return returnFile

def import_csv(filename):
    returnFile=[]
    with open(filename, encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            returnFile.append(row) 
        return returnFile

def export_csv(filename,header,data):
    writer = createCSVHeader(filename,header)
    
    for row in data:

        writer.writerow(row)

