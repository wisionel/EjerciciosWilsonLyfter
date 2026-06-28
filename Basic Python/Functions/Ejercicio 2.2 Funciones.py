my_number= 4

def fun():
    global my_number
    my_number= my_number+4
    print(my_number)

fun()


#si no hubiera usado global saldria un error que dice cannot access local variable