import csv
from wsgiref import headers

dataset1=[]
dataset2=[]

with open("final.csv","r") as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        dataset1.append(row)

with open("planetarchive.csv","r") as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        dataset2.append(row)

headers1=dataset1[0]
planet_data1=dataset1[1:]

headers2=dataset2[0]
planet_data2=dataset2[1:]

header=headers1+headers2
planet_data=[]

for index,data_row in enumerate(planet_data1):
    planet_data.append(planet_data1[index]+planet_data2[index])
    
with open("mergeddata.csv","a+")as f:
    writer=csv.writer(f)
    writer.writerow(header)
    writer.writerows(planet_data)

with open("mergeddata.csv")as input,open("final1.csv",'w',newline='')as output:
    writer=csv.writer(output)
    for row in csv.reader(input):
        if any(field.strip()for field in row):
            writer.writerow(row)


