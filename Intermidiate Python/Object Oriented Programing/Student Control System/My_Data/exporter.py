import csv

def csv_creator(path,my_list):
    data=[]
    for student in my_list:
        new_dict={}
        new_dict["Nombre Completo"]= student.name
        new_dict["Seccion"]= student.section
        new_dict["Nota Español"]= student.spanish
        new_dict["Nota Ingles"]= student.english
        new_dict["Nota Estudios Sociales"]= student.social_studies
        new_dict["Nota Ciencias"]= student.science
        new_dict["Nota Promedio"]= student.average
        data.append(new_dict)

    with open (path,'w', encoding='utf-8', newline='') as file:
        headers="Nombre Completo","Seccion","Nota Español","Nota Ingles","Nota Estudios Sociales","Nota Ciencias","Nota Promedio"
        writer= csv.DictWriter(file,fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)


