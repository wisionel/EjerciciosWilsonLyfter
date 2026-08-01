class Rectangle:
    def __init__(self,width,height):
        self.width=None
        self.height=None
        try:
            self.width=width
            self.height=height
            if height < 0:
                raise Exception()
            elif width < 0:
                raise Exception()
        except Exception:
            print("El valor no puede ser negativo") 

    def get_area(self):
        area=self.width*self.height
        print(area)
        return area

    def get_perimeter(self):
        perimeter=2*(self.width+self.height)
        print(perimeter)
        return perimeter


rectangle_1=Rectangle(2,2)
rectangle_1.get_area()
rectangle_1.get_perimeter()
