def my_sum(number):
    global current_number
    addend=0
    try:
        addend=int(input("Ingrese numero a sumar "))
    except ValueError as ex:
        print(f"Ingrese un numero valido, error:{ex}")
        raise 
    result=number+addend
    current_number=result
    return current_number

def difference(number):
    global current_number
    subtrahend=0
    try:
        subtrahend=int(input("Ingrese numero a restar "))
    except ValueError as ex:
        print(f"Ingrese un numero valido, error:{ex}")
        raise
    result=number-subtrahend
    current_number=result
    return current_number


def multipication(number):
    global current_number
    product=0
    try:
        product=int(input("Ingrese numero a multiplicar "))
    except ValueError as ex:
        print(f"Ingrese un numero valido, error:{ex}")
        raise
    result=number*product
    current_number=result
    return current_number


def division(number):
    global current_number
    divisor=1
    try:
        divisor=int(input("Ingrese numero a dividir "))
        if divisor==0:
            raise ZeroDivisionError()
    except ValueError as ex:
        print(f"Ingrese un numero valido, error:{ex}")
        raise
    except ZeroDivisionError as ex:
        print(f"Numero no se puede dividir entre 0:{ex}")
        raise
    result=number/divisor
    current_number=result
    return current_number


def clear_result(number):
    global current_number
    current_number=0
    main(current_number)



def main(number):
    try:
        print(f"Numero Actual: {number}")        
        menu={
            1: "suma",
            2: "resta",
            3: "multiplicacion",
            4: "division",
            5: "borrar resultado",
            6:"finalizar operacion"
            }
        print("Operaciones")
        print(menu)
        action=int(input("Ingrese la operacion que quiere hacer "))
        if action==1:
            my_sum(number)
        elif action==2:
            difference(number)
        elif action==3:
            multipication(number)
        elif action==4:
            division(number)
        elif action==5:
            clear_result(number)
        elif action==6:
            print(f"El resultado es {current_number}")
            exit()
        elif action<1 or action>6:    
            raise KeyError()
        print(f"Resultado:{current_number}")
        main(current_number)
    except ValueError as ex:
        print(f"Ingrese un valor valido, error:{ex}")
        main(current_number)
    except KeyError as ex:
        print(f"Ingrese una opcion valida")
        main(current_number)
    except Exception as rex:
        main(current_number)
    


try:
    current_number=int(input("Ingrese un numero "))
except ValueError as ex:
    print(f"Ingrese un valor valido, error:{ex}")
    current_number=int(input("Ingrese un numero "))



main(current_number)