def cap_converter(path):
    upper_list=[]
    with open(path,'r',encoding='utf-8') as file:
        content= file.readlines()
        for item in content:
            cap_item=item.upper()
            upper_list.append(cap_item)
    return upper_list


def new_file_creator(name,my_list):
    with open(name,'w',encoding='utf-8') as file:
        file.writelines(my_list)


def main(path):
    cap_list=cap_converter(path)
    file_name=input("Ingrese el nombre del nuevo archivo")
    new_file_creator(file_name,cap_list)


main("Ejercicio Extra 3.txt")