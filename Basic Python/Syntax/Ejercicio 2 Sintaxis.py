name= input("Inserte su Nombre")
last_name= input("Inserte su Apellido")
age= int(input("Inserte su Edad"))
if age<=5:
    print("eres un bebe")
elif 5<age<10:
    print("eres un niño")
elif 10<=age<14:
    print("eres un preadolescente")
elif 14<=age<18:
    print("eres un adolescente")
elif 18<=age<35:
    print("eres un adulto joven")
elif 35<=age<65:
    print("eres un adulto")
elif age>=65:
    print("eres un adulto mayor")
