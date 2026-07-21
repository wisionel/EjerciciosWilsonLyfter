def student_name():
    my_name=input("Ingrese el nombre del estudiante ")
    return my_name


def student_section():
    my_section=input("Ingrese la seccion del estudiante ")
    return my_section


def spanish():
    my_grade=None
    try:
        my_grade=int(input("Ingrese la nota de español "))
        if my_grade <0 or my_grade>100:
            raise ValueError()
    except ValueError:
        print("Ingrese un valor entre 1-100")
        return spanish()
    return my_grade


def english():
    my_grade=None
    try:
        my_grade=int(input("Ingrese la nota de ingles "))
        if my_grade <0 or my_grade>100:
            raise ValueError()
    except ValueError:
        print("Ingrese un valor entre 1-100")
        return english()
    return my_grade


def social_studies():
    my_grade=None
    try:
        my_grade=int(input("Ingrese la nota de estudios sociales "))
        if my_grade <0 or my_grade>100:
            raise ValueError()
    except ValueError:
        print("Ingrese un valor entre 1-100")
        return social_studies()
    return my_grade


def science():
    my_grade=None
    try:
        my_grade=int(input("Ingrese la nota de ciencia "))
        if my_grade <0 or my_grade>100:
            raise ValueError()
    except ValueError:
        print("Ingrese un valor entre 1-100")
        return science()
    return my_grade


def student_inputer():
    student_list=[]
    counter=1
    student_quantity=0
    try:
        student_quantity=int(input("Ingrese la cantidad de estudiantes a ingresar "))
    except ValueError:
        print("Ingrese un valor valido")
        student_inputer()
    while counter<= student_quantity:
        student_dictionary={}
        student_dictionary["Nombre Completo"]=student_name()
        student_dictionary["Seccion"]=student_section()
        student_dictionary["Nota Español"]=spanish()
        student_dictionary["Nota Ingles"]=english()
        student_dictionary["Nota Estudios Sociales"]=social_studies()
        student_dictionary["Nota Ciencias"]=science()
        student_dictionary["Nota Promedio"]=(student_dictionary["Nota Español"] + student_dictionary["Nota Ingles"] + student_dictionary["Nota Estudios Sociales"] + student_dictionary["Nota Ciencias"])/4
        student_list.append(student_dictionary)
        counter+=1
    return student_list
