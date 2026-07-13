import csv

def student_importer(path):
    with open (path,'r',encoding='utf-8') as file:
        reader=csv.DictReader(file)
        new_list=[]
        for line in reader:
            new_list.append(line)
        return new_list

