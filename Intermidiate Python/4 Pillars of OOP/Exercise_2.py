from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        super().__init__()
        self.radius=radius

    def calculate_area(self):
        area= 3.14*self.radius**2
        print(f"El area del circulo es de {area}")
        return area

    def calculate_perimeter(self):
        perimeter=3.14*self.radius*2
        print(f"El perimetro del circulo es de {perimeter}")
        return perimeter

class Square(Shape):
    def __init__(self,side):
        super().__init__()
        self.side=side

    def calculate_perimeter(self):
        perimeter=4*self.side
        print(f"El perimetro del cuadrado es de {perimeter}")
        return perimeter
    
    def calculate_area(self):
        area=self.side**2
        print(f"El area del cuadrado es de {area}")
        return area

class Rectangle(Shape):
    def __init__(self,length,width):
        super().__init__()
        self.length=length
        self.width=width

    def calculate_area(self):
        area= self.length*self.width
        print(f"El area del rectangulo es de {area}")
        return area

    def calculate_perimeter(self):
        perimeter=(2*self.length)+(2*self.width)
        print(f"El perimetro del rectangulo es de {perimeter}")
        return perimeter

circle_1=Circle(5)
circle_1.calculate_perimeter()
circle_1.calculate_area()
square_1=Square(5)
square_1.calculate_area()
square_1.calculate_perimeter()
rectangle_1=Rectangle(5,6)
rectangle_1.calculate_perimeter()
rectangle_1.calculate_area()
