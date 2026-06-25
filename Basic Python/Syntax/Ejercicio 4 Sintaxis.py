number1=int(input("Inserte el primer numero"))
number2=int(input("Inserte el segundo numero"))
number3=int(input("Inserte el tercer numero"))
list= [number1,number2,number3]
largest=list[0]
for n in list:
    if n>largest:
        largest=n
print(largest)


