import csv


def file_reader(path):
    with open(path,'r',encoding='utf-8') as file:
        reader=csv.reader(file)
        next(reader)
        for line in reader:
            print(f"Nombre: {line[0]}")
            print(f"Genero: {line[1]}")
            print(f"Desarrollador: {line[2]}")
            print(f"Clasificacion ESRB: {line[3]}")
            print("")


file_reader("Video game list.csv")