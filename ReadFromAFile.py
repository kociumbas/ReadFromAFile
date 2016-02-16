import csv

fileName = "GuestsList.txt"
accessMode = "r"

with open(fileName, accessMode) as myCSVFile:
    dataFromFile = csv.reader(myCSVFile)
    for row in dataFromFile:
        print (", ".join(row))  #removes square brackets by joining list items