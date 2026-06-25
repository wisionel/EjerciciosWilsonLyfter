list=[1,2,3,4,5,6]
first=list[0]
last=list[len(list)-1]
list[0]=last
list[len(list)-1]=first
print(list)