def upper_counter(my_string):
    upper_counter=0
    for letter in my_string:
        if letter.isupper():
            upper_counter+=1
    print(f"Hay {upper_counter} de mayusculas")
    return upper_counter
    


def lower_counter(my_string):
    lower_counter=0
    for letter in my_string:
        if letter.islower():
            lower_counter+=1
    print(f"Hay {lower_counter} de minusculas")       
    return lower_counter
    


def main(word):
    upper_counter(word)
    lower_counter(word)


my_string="Hola yo soy Wilson"
main(my_string)
