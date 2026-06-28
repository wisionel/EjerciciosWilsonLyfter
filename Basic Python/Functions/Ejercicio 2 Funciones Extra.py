def list_creator():
    counter=0
    my_list=[]
    while counter<5:
        my_list.append(input("Ingrese palabra "))
        counter+=1
    return my_list


def word_printer(word_list,n):
    list_2=[]
    for word in range(len(word_list)):
        if len(word_list[word])>n:
            list_2.append(word_list[word])
    print(word_list)
    print(list_2)


list_of_words=list_creator()
number_of_letters=int(input("Ingrese numero de letras"))

word_printer(list_of_words,number_of_letters)

