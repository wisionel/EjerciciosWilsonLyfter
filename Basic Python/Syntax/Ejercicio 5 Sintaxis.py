grade_counter= 1
approved_grades=0
disapproved_grades=0
sum_approved_grades=0
sum_disapproved_grades=0
average_grades=0
avereage_disapproved_grades=0
average_approved_grades=0
total_grades= int(input("ingrese la cantidad de notas"))
while grade_counter <= total_grades:
    print(grade_counter)
    grade=int(input("ingrese la nota"))
    if grade<70:
        disapproved_grades= disapproved_grades + 1
        sum_disapproved_grades= sum_disapproved_grades + grade 
        avereage_disapproved_grades= sum_disapproved_grades/disapproved_grades
        
    else:
        approved_grades= approved_grades + 1
        sum_approved_grades= sum_approved_grades + grade
        average_approved_grades= sum_approved_grades/approved_grades
        
    average_grades= average_grades + (grade/total_grades)
    grade_counter= grade_counter + 1

    
    
if sum_approved_grades>0:
    print(f"El estudiante tiene esta cantidad de notas aprobadas {approved_grades}")
    print(f"Este es el promedio de notas aprobadas{average_approved_grades}")
else: 
    print("No hay notas aprobadas")
if sum_disapproved_grades>0:
    print(f"El estudiante tiene esta cantidad de notas desaprobadas{disapproved_grades}")
    print(f"Este es el promedio de notas desaprobadas{avereage_disapproved_grades}")
else:
    print("No hay notas desaprobadas")
print(f"Este es el promedio de notas {average_grades}")
