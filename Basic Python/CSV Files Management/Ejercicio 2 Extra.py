import csv

def class_finder(ESRB,path):
    ESRB_list=[]
    with open(path,'r',encoding='utf-8') as file:
        reader=csv.DictReader(file)
        
        for line in reader:
            if line['Clasificacion ESRB']== ESRB:
                ESRB_list.append(line["Nombre"])
    return ESRB_list


def main(path):
    my_ESRB=input("Ingrese la clasificacion de ESRB ").upper()
    ESRB_list=class_finder(my_ESRB,path)
    print(f"Los siguientes juegos tienen la clasificacion {my_ESRB}: ")
    for game in ESRB_list:
        print(game)
main("Video game list.csv")
