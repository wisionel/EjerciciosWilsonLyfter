class Circle:
    def get_area(self):
        self.radius=int(input("Ingrese el radio "))
        area=3.14*self.radius**2
        print(f"El area del circulo es de {area}")
        return area


circle_1=Circle()
circle_1.get_area()
circle_2=Circle()
circle_2.get_area()