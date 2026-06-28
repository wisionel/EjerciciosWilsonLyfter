list=[]
list2=[]
counter=1
while counter<=5:
    word=input("Ingrese palabra ")
    list.append(word)
    counter+=1
for letter in range(len(list)):
    if len(list[letter])>4:
        list2.append(list[letter])
print(list2)    