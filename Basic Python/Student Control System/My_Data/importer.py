import csv

def student_importer(path):
    with open (path,'r',encoding='utf-8') as file:
        reader=csv.DictReader(file)
        new_list=[]
        for line in reader:
            line["Nota Español"]=float(line["Nota Español"])
            line["Nota Ingles"]=float(line["Nota Ingles"])
            line["Nota Estudios Sociales"]=float(line["Nota Estudios Sociales"])
            line["Nota Ciencias"]=float(line["Nota Ciencias"])
            line["Nota Promedio"]=float(line["Nota Promedio"])
            new_list.append(line)
        return new_list

