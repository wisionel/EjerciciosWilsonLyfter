list=[1,2,3,4,5,6]
first=list[0]
last=list[len(list)-1]
for number in range(len(list)):
    list[0]=last
    list[len(list)-1]=first
print(list)