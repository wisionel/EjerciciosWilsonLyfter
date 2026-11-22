def is_number(func):
    def wrapper(number_1,number_2):
        try:
            number_1=int(number_1)
            number_2=int(number_2)
            func(number_1,number_2)
        except ValueError as error:
            raise ValueError("No se puede sumar valores no numerales")
    return wrapper
    


@is_number
def add(number_1,number_2):
    result=number_1+number_2
    print(result)

def main(number_1,number_2):
    add(number_1,number_2)
    

main("d",2)
