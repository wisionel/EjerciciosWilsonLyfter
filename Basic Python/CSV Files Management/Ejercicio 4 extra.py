import csv

def game_finder(path,publisher):
    game_list=[]
    with open(path,'r',encoding='utf-8') as file:
        reader=csv.DictReader(file)

        for line in reader:
            if line["Desarrollador"]==publisher:
                print(f"{line["Nombre"]} (ESRB:{line["Clasificacion ESRB"]}, Genero:{line["Genero"]})")


def main(path):
    my_publisher=input("Ingrese el desarrollador ")
    print(f"Estos son los videojuegos desarrollados por {my_publisher}")
    game_finder(path,my_publisher)



main("Video game list.csv")