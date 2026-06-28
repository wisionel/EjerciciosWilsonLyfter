def string_appender(my_file,my_string):
    try:
        with open(my_file,'x',encoding='utf-8') as file:
            file.write(my_string)
    except FileExistsError:
        with open(my_file,'a',encoding='utf-8') as file:
            file.write("\n"+my_string)


def main():
    new_file=input("Ingrese el nombre del archivo nuevo ")
    new_string=input("Ingrese linea de texto ")
    string_appender(new_file,new_string)


main()