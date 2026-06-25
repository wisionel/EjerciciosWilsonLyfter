def my_sum(number):
    addend=0
    try:
        addend=int(input("Ingrese numero a sumar "))
    except ValueError as ex:
        print(f"Ingrese un numero valido, error:{ex}")
        exit()
    result=number+addend
    return result

def difference(number):
    subtrahend=0
    try:
        subtrahend=int(input("Ingrese numero a restar "))
    except ValueError as ex:
        print(f"Ingrese un numero valido, error:{ex}")
        exit()
    result=number-subtrahend
    return result


def multipication(number):
    product=0
    try:
        product=int(input("Ingrese numero a multiplicar "))
    except ValueError as ex:
        print(f"Ingrese un numero valido, error:{ex}")
        exit()
    result=number*product
    return result


def division(number):
    divisor=1
    try:
        divisor=int(input("Ingrese numero a dividir "))
        if divisor==0:
            raise ZeroDivisionError()
    except ValueError as ex:
        print(f"Ingrese un numero valido, error:{ex}")
        exit()
    except ZeroDivisionError as ex:
        print(f"Numero no se puede dividir entre 0:{ex}")
        exit()
    result=number/divisor
    return result


def clear_result(number):
    number=None
    main()



def main():
    try:
        global my_number
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
        options={
            1:my_sum,
            2:difference,
            3:multipication,
            4:division,
            5:clear_result
            }
        result=options[action]
        print(result)

        my_number=result(my_number)
        print(my_number)
        return my_number
    except ValueError as ex:
        print(f"Ingrese un valor valido, error:{ex}")
    except KeyError as ex:
        print(f"Seleccione una opcion valida, error:{ex}")

main()
