from Actions.Students import student_inputer
from Actions.Student_Info import student_printer
from Actions.Student_Average import average_students
from My_Data.exporter import csv_creator
from Actions.Top_3 import top3_maker

def my_menu2(my_list):
    print("Menu")
    print("Seleccione uno de las siguientes opciones")
    print("1-Ver informacion de todos los estudiantes")
    print("2-Ver nota promedio de cada estudiantes")
    print("3-Mostrar el top 3 de estudiantes")
    print("4-Exportar datos")
    print("5-Finalizar operacion")
    action_2=None
    try:
        action_2= int(input("Ingrese la operacion que desea hacer "))
        if action_2 <1 or action_2>5:
            raise ValueError()
    except ValueError:
            print("Ingrese una opcion valida")
    if action_2==1:
        student_printer(my_list)
        my_menu2(my_list)
    elif action_2==2:
        average_students(my_list)
        my_menu2(my_list)
    elif action_2==3:
        top_3=top3_maker(my_list)
        for student in top_3:
            print(student)
        my_menu2(my_list)
    elif action_2==4:
        path= input("Ingrese el nombre que desea ponerle a la lista" ) + ".csv"
        csv_creator(path,my_list)
        my_menu2(my_list)
    elif action_2==5:
        exit()
