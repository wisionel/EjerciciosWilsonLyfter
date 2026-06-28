import csv

with open("Video Game list.csv",'r',encoding='utf-8') as file:
    reader=csv.DictReader(file)
    rows= list(reader)
    print(rows)

