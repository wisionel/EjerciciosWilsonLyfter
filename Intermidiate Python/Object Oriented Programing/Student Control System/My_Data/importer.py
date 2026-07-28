import csv

def student_importer(path):
    with open (path,'r',encoding='utf-8') as file:
        reader=csv.DictReader(file)
        new_list=[]
        for line in reader:
            class Student:
                def __init__(self):
                    self.name=line["Nombre Completo"]
                    self.section=line["Seccion"]
                    self.spanish=float(line["Nota Español"])
                    self.english=float(line["Nota Ingles"])
                    self.social_studies=float(line["Nota Estudios Sociales"])
                    self.science=float(line["Nota Ciencias"])
                    self.average=(self.spanish + self.english + self.social_studies + self.science)/4
            line= Student()
            new_list.append(line)
        return new_list
        

