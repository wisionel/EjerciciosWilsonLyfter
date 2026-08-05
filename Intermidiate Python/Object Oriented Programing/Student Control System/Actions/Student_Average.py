def average_students(my_list):
    new_list=[]
    for students in my_list:
        new_list.append(float(students.average))
    whole_average=sum(new_list)/len(new_list)
    print(f"El promedio de todos los estudiantes es de {whole_average}")

