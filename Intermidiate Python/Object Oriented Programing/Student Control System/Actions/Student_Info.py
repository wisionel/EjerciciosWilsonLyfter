def student_printer(my_dict):
    for student in my_dict:
        print (f"Nombre: {student.name}, Seccion: {student.section}, Español: {student.spanish}, Ingles: {student.english}, Estudios Sociales: {student.social_studies}, Ciencias: {student.science}, Promedio: {student.average}")
        