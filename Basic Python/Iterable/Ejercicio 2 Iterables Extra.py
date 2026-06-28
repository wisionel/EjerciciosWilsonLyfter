number=[1,2,6,5,-8,-50,10,50]
negative_counter=0
for num in range(len(number)):
    if number[num]<=0:
        negative_counter+=1

result=f"Hay {negative_counter} numeros negativos o ceros en la lista"
result2="Todos los numeros de la lista son positivos"

if negative_counter>0:
    print(result)
else:
    print(result2)
