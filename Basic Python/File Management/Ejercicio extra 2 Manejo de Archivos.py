def list_converter(path):
    with open(path,'r',encoding="utf-8") as file:
        content=file.read()
        new_list=content.split()
    return new_list


def list_counter(list):
    word_quantity=len(list)
    print(f"Este archivo contiene {word_quantity} palabras")
    return word_quantity


def main(path):
    my_list=list_converter(path)
    list_counter(my_list)


main("Ejercicio extra 2.txt")