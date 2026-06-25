import csv


def video_games_catalog(data):
    path=input("Ingrese el nombre del archivo nuevo ")
    with open(path,'w',encoding='utf-8',newline="") as file:
        headers="Nombre","Genero","Desarrollador","Clasificacion ESRB"
        writer=csv.DictWriter(file,delimiter="\t",fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

def list_creator(quantity):
    game_list=[]
    counter=1
    while counter <= quantity:
        my_dict={}
        my_dict['Nombre']=input('Ingrese el nombre del juego ')
        my_dict['Genero']=input('Ingrese el genero del juego ')
        my_dict['Desarrollador']=input('Ingrese el desarrollador del juego ')
        my_dict['Clasificacion ESRB']=input('Ingrese el ESRB del juego ')
        game_list.append(my_dict)
        counter+=1
    return game_list


def main():
    quantity_of_games=int(input("Ingrese la cantidad de juegos "))
    video_game_list= list_creator(quantity_of_games)
    video_games_catalog(video_game_list)


main()
