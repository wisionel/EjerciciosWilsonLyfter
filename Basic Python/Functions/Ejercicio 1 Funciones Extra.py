def character_finder(word,letter):
    counter=0
    for cha in range(len(word)):
        if word[cha]==letter:
            counter+=1
    print(f"La letra {letter} aparece {counter} veces en {word}")
    return counter


my_word=input("Ingrese palabra ")
specific_letter=input("Ingrese letra a buscar ")

character_finder(my_word,specific_letter)
