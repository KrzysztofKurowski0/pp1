import csv
with open("students.csv","r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    linecount=0
    for row in csv_reader:
        if linecount==0:
            linecount+=1
        else:
            if int(row[2])<30:
                print(row[0],row[1],row[4])
            else:
                continue
            
