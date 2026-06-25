number=int(input("ingrese numero"))
counter=0
sum_remainders=0
remainder=number-counter
while remainder>0: 
    remainder=number-counter
    sum_remainders=sum_remainders+remainder
    counter=counter+1

print(sum_remainders)


