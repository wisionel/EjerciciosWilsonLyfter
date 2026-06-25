def file_reader(path):
    with open(path,'r',encoding='utf-8') as file:
        content=file.readlines()
        print(content)
    return content


def string_creator(list):
    new_list=[]
    for item in range(len(list)):
        new_item=list[item].strip('\n')
        new_list.append(new_item)
    new_string=" ".join(new_list)
    print(new_string)
    return new_string


def new_file_creator(file_name,text):
    with open(file_name,'w',encoding='utf-8') as file:
        file.write(text)


def main(path):
    my_file=input("Ingrese el nombre del archivo")
    my_list=file_reader(path)
    my_string=string_creator(my_list)
    new_file_creator(my_file,my_string)


main("Ejercicio extra 1.txt")