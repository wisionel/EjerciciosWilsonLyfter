def integer_finder(list):
    for item in range(len(list)):
        try:        
            int(list[item])
            print(f"{list[item]} fue convertido")
        except ValueError:
            print(f"No se pudo convertir el elemento: {list[item]} ")


my_list=["5","88","Hola","What"]

integer_finder(my_list)