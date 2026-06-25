def multiply_by_5():
    result=ask_number() * 5
    print(f"el resultado es {result}")
    return result
def ask_number():
    number=int(input("Ingrese Numero"))
    print(f"el numero escogido fue {number}")
    return number

multiply_by_5() 