from Menu.Menu_1 import my_menu1
from Menu.Menu_2 import my_menu2
from Actions.Students import student_inputer
from My_Data.importer import student_importer

def main():
    my_menu1()
    action=None
    try:
        action=int(input("Ingrese la operacion que desea hacer "))
        if action <1 or action>2:
            raise ValueError()
    except ValueError:
        print("Ingrese una opcion valida")
        main()
    if action==1:
        student_dictionary=student_inputer()
        my_menu2(student_dictionary)
    if action==2:
        file_name=input("Ingrese el nombre de la lista ") + ".csv"
        student_dictionary2=None
        try:
            student_dictionary2=student_importer(file_name)
            my_menu2(student_dictionary2)
        except FileNotFoundError:
            print("La lista no se puede encontrar")
            main()


main()
