class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=int(price)
        self.quantity=int(quantity)

class Inventory:
    def __init__(self):
        self.inventory_list=[]
    def add(self,product):
        self.inventory_list.append(product)
        print(f"Se ha agregado {product.name} al inventario")

    def show(self):
        print(f"El inventario contiene los siguientes productos:")
        my_list=[]
        for product in self.inventory_list:
            my_list.append(product.name)
        print(my_list)

    def inventory_value(self):
        product_value=[]
        for product in self.inventory_list:
            value=product.price * product.quantity
            product_value.append(value)
        total_value=sum(product_value)
        print(f"El valor total del inventario es {total_value}")

product_1=Product("Huevo",10,3)
product_2=Product("Leche",5,2)
product_3=Product("Chile",2,5)
my_inventory=Inventory()
my_inventory.add(product_1)
my_inventory.add(product_2)
my_inventory.add(product_3)
my_inventory.show()
my_inventory.inventory_value()