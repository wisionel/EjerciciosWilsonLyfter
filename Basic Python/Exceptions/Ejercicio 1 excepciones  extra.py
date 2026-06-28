def name_asker(name):
    if name.isdigit():
        raise ValueError("El nombre no puede ser un numero")


def age_asker():
    age=None
    try:
        age=int(input("Ingrese su edad "))
    except ValueError:
        print("Numero no valido")
    return age


def result(name,age):
    print(f"Hola {name} su edad es {age}")
    

def main(name):
    try:
        name_asker(name)
        my_age=age_asker()
        result(name,my_age)    
    except ValueError:
        print("El nombre no puede ser un numero")


my_name=input("Ingrese su nombre ")

main(my_name)