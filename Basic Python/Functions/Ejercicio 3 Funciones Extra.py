def vocal_counter(string):
    counter=0
    for letter in string:
        if letter == "a":
            counter+=1
        elif letter == "e":
            counter+=1
        elif letter == "i":
            counter+=1
        elif letter == "o":
            counter+=1
        elif letter == "u":
            counter+=1
        if letter == "A":
            counter+=1
        elif letter == "E":
            counter+=1
        elif letter == "I":
            counter+=1
        elif letter == "O":
            counter+=1
        elif letter == "U":
            counter+=1
    print(f"La palabra u oracion contiene {counter} vocales")


my_string=input("Inserte palabra u oracion ")
vocal_counter(my_string)
