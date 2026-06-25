time= int(input("ingrese tiempo en en segundos"))
if time<600: 
    remaining_time= 600 - time
    print(f"el tiempo restante para llegar a 10 minutos es {remaining_time}")
    
elif time>600:
    print("mayor")
elif time==600:
    print("igual")