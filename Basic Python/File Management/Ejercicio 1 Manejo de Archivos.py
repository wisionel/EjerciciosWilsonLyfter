def list_appender(path):
    with open(path,'a',encoding='utf-8') as file:
        file.write('\n')

def read_songs(path):
    with open(path,'r',encoding='utf-8') as file:
        songs= file.readlines()
    return songs


def song_organizer(list):
    sorted_list= sorted(list)
    return sorted_list


def new_list_creator(output_path,list):
    with open(output_path,'w',encoding='utf-8') as file:
        file.writelines(list)


def main(path):
    list_appender(path)
    song_list=read_songs(path)
    sorted_songs=song_organizer(song_list)
    new_path=input("Ingrese el nombre del nuevo archivo")
    new_list_creator(new_path,sorted_songs)



main('canciones.txt')