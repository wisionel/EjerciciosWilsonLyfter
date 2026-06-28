def my_sum(number):
    global my_number
    addend=0
    try:
        addend=int(input("Ingrese numero a sumar "))
    except ValueError as ex:
        print(f"Ingrese un numero valido, error:{ex}")
        raise 
    result=number+addend
    my_number=result
    print(my_number)
    return result

def difference(number):
    global my_number
    subtrahend=0
    try:
        subtrahend=int(input("Ingrese numero a restar "))
    except ValueError as ex:
        print(f"Ingrese un numero valido, error:{ex}")
        raise
    result=number-subtrahend
    my_number=result
    print(my_number)
    return result


def multipication(number):
    global my_number
    product=0
    try:
        product=int(input("Ingrese numero a multiplicar "))
    except ValueError as ex:
        print(f"Ingrese un numero valido, error:{ex}")
        raise
    result=number*product
    my_number=result
    print(my_number)
    return result


def division(number):
    global my_number
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
    my_number=result
    print(my_number)
    return result


def clear_result(number):
    number=None
    main()



def main():
    try:
        my_number=int(input("Ingrese un numero "))
        menu={
            1: "suma",
            2: "resta",
            3: "multiplicacion",
            4: "division",
            5: "borrar resultado"
            }
        print("Operaciones")
        print(menu)
        action=int(input("Ingrese la operacion que quiere hacer "))
        if action==1:
            my_sum(my_number)
        elif action==2:
            difference(my_number)
        elif action==3:
            multipication(my_number)
        elif action==4:
            division(my_number)
        elif action==5:
            clear_result(my_number)
        if action<1 or action>5:    
            raise KeyError()
    except ValueError as ex:
        print(f"Ingrese un valor valido, error:{ex}")
        main()
    except KeyError as ex:
        print(f"Ingrese una opcion valida")
        main()
    except Exception as rex:
        main()



main()