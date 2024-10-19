"""
path = "C:\\Users\\Alakh Pandya\\Desktop\\Batches\\Ashesh One_to_one US\\GoogleStockData.csv"
file = open(path)
# print(file.read())
# print(file)
# for row in file:
#     print(row)
dataList = file.readlines()
# print(len(dataList))
print(dataList[0].strip().split(","))
print(dataList[1].strip().split(","))
# print(dataList)

dataSet = [row.strip().split(",") for row in dataList]
# for row in dataList:
#     dataSet.append(row.strip().split(","))
print(dataSet)

file.close()
"""
"""
file = open("myCollection.csv")
dataList = file.readlines()
dataSet = [row.strip().split(",") for row in dataList]
print(dataSet)
file.close()
"""
"""
import csv
path = "C:\\Users\\Alakh Pandya\\Desktop\\Batches\\Ashesh One_to_one US\\GoogleStockData.csv"
file = open(path, newline="")
for row in csv.reader(file):
    print(row)

file.close()
"""
# import csv

# file = open("myCollection.csv")
# reader = csv.reader(file)
# heading = next(reader)
# for row in reader:
#     print(row)
# file.close()

import csv
from datetime import datetime

file = open("GoogleStockData.csv")
reader = csv.reader(file)
heading = next(reader)
for row in reader:
    row[0] = datetime.strptime(row[0], '%m/%d/%Y')
    row[1] = float(row[1])
    row[2] = float(row[2])
    row[3] = float(row[3])
    row[4] = float(row[4])
    row[5] = int(row[5])
    row[6] = float(row[6])
    print(row[0])
file.close()