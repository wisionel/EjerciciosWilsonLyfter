class Vehicle:
    def __init__(self,brand,year):
        self._brand=brand
        self.year=year

    def get_info(self):
        print(f"Marca:{self._brand}")
        print(f"Año:{self.year}")

class Car(Vehicle):
    def __init__(self, brand, year,door):
        super().__init__(brand, year)
        self.door=door

    def get_info(self):
        super().get_info()
        print(f"{self.door} Puertas")

class Motorcycle(Vehicle):
    def __init__(self, brand, year,type):
        super().__init__(brand, year)
        self.type=type

    def get_info(self):
        super().get_info()
        print(f"Tipo: {self.type}")

car_1=Car("Hyundai",2025,4)
car_1.get_info()
motorcycle_1=Motorcycle("Suzuki",2023,"Motocross")
motorcycle_1.get_info()