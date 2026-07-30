class Circle:
    def __init__(self, radius):
        self.radius=radius
    def get_area(self):
        area=3.14*self.radius**2
        print(f"El area del circulo es de {area}")
        return area


circle_1=Circle(5)
circle_1.get_area()
circle_2=Circle(6)
circle_2.get_area()