def is_number(func):
    def wrapper(number_1,number_2):
        try:
            number_1=int(number_1)
            number_2=int(number_2)
        except ValueError:
            print("No se puede sumar valores no numerales")
        func(number_1,number_2)
    return wrapper
    


@is_number
def add(number_1,number_2):
    result=None
    try:
        result=number_1+number_2
    except TypeError:
        raise Exception()
    print(result)

def main(number_1,number_2):
    try:
        add(number_1,number_2)
    except Exception:
        print("No se puede sumar valores no numerales")

main("d",2)
