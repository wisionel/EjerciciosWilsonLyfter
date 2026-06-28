list=[]
counter=1
while counter<6:
    number1=int(input("Ingrese Numero"))
    list.append(number1)
    counter +=1
specific_number=int(input("Inserte numero a buscar"))
specific_number_counter=0
for number in list:
    if number==specific_number:
        specific_number_counter+=1
result=f"El numero {specific_number} aparece {specific_number_counter} veces en la lista"
print(result)
