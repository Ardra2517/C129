import csv

dataset_1 = []
dataset_2 = []

with open("final.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        dataset_1.append(row)

#1)open archive_dataset_sorted1.csv
with open("archive_dataset_sorted1.csv","r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset_2.append(row)

#data from final.csv
headers_1 = dataset_1[0]
planet_data_1 = dataset_1[1:]

#2)data from archive_dataset_sorted1.csv
headers_2 = dataset_2[0]
planet_data_2 =  dataset_2[1:]


#Final outcome of both the sheets
headers = headers_1 + headers_2
planet_data = []

for index, data_row in enumerate(planet_data_1):
    planet_data.append(planet_data_1[index] + planet_data_2[index])

#3)Open a new file and add the merged data
with open("merge.csv","a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)
    