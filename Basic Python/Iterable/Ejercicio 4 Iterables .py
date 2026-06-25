list=[1,2,3,4,5,6]
even_number=[]
for number in range(len(list)):
    if list[number]%2==0:
        even_number.append(list[number])
print(even_number)