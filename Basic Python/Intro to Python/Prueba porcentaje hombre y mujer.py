sum_man=0
sum_women=0
counter=1
print("ingrese 1 para mujer y 2 para hombre")
while counter <= 6:
    print(counter) 
    number=int(input("Enter 1 or 2"))
    counter += 1
    if number==1:
        sum_women=sum_women+1
    elif number==2:
        sum_man=sum_man+1
    elif number != 1 and 2:
        print("ingrese 1 para mujer y 2 para hombre")
        break
women_percentage=sum_women/6*100
men_percentage=sum_man/6*100
result_women=f"the percentage of women is {women_percentage}%"
result_men=f"the percentage of men is {men_percentage}%"
print(result_men)
print(result_women)

