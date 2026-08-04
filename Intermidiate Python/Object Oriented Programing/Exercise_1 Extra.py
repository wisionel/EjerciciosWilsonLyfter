class Rectangle:
    def __init__(self):
        self.width=int(input("Ingrese el valor "))
        self.height=int(input("Ingrese el valor "))
        if self.height < 0:
            raise Exception()
        elif self.width < 0:
            raise Exception()

    def get_area(self):
        area=self.width*self.height
        print(area)
        return area

    def get_perimeter(self):
        perimeter=2*(self.width+self.height)
        print(perimeter)
        return perimeter

try:
    rectangle_1=Rectangle()
    rectangle_1.get_area()
    rectangle_1.get_perimeter()
except ValueError:
    print("Ingrese un valor valido")
except Exception:
    print("El valor no puede ser negativo") 
