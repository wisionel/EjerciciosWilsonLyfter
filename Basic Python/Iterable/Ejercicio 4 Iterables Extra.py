list=[50,68,90,80,95,100,45]
list2=[]
average=sum(list)/len(list)
print(f"Promedio= {average}")
for num in range(len(list)):
    if list[num]>average:
        list2.append(list[num])
print(f"Los numeros mayores al promedio son {list2}")