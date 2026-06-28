def factor_counter(number):
    factors=[]
    for i in range(1,number+1):
        if number%i==0:
            factors.append(i)
    return len(factors)


def prime_list_creator(list): 
    prime_numbers=[]
    for number in list:
        if factor_counter(number)==2:
            prime_numbers.append(number)
    if prime_numbers==[]:
        print("No hay numeros primos")
    else:
        print(prime_numbers)


my_list=[2,3,4,8,10]   

prime_list_creator(my_list) 

