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

class Student:
    def __init__(self):
        self.name=student_name()
        self.section=student_section()
        self.spanish=spanish()
        self.english=english()
        self.social_studies=social_studies()
        self.science=science()
        self.average=(self.spanish + self.english + self.social_studies + self.science)/4

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
        my_student=Student()
        student_list.append(my_student)
        counter+=1
    return student_list


