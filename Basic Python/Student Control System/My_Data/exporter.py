import csv

def csv_creator(path,data):
    with open (path,'w', encoding='utf-8', newline='') as file:
        headers="Nombre Completo","Seccion","Nota Español","Nota Ingles","Nota Estudios Sociales","Nota Ciencias","Nota Promedio"
        writer= csv.DictWriter(file,fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)


