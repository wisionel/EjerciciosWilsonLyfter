import random
random_number= random.randint(1,10)
number=int(input("Inserte Numero"))
while number!=random_number:
    number=int(input("Inserte otro numero"))
print("Numero Correcto")
