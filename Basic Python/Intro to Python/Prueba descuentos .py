price= int(input("inserte el precio"))
if price < 100:
    discount= price * 0.02
else:
    discount= price * 0.1
final_price= price - discount
print(f"el precio final es de {final_price}")

