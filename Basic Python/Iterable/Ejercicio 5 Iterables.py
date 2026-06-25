list=[]
counter=1
while counter<=10:
    number1=int(input("Ingrese Numero"))
    list.append(number1)
    counter+=1
biggest_number=list[0]
for n in list:
    if n>biggest_number:
        biggest_number=n
print(f"{list}el numero mas alto es {biggest_number}")
