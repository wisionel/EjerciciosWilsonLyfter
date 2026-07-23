class Bus:
    max_passengers=2
    passengers=[]

    def onboard(self,person):
        if len(self.passengers)>= self.max_passengers:
            print("Ya no hay mas espacio en el bus")
        else:
            self.passengers.append(person)
            print(f"{person} se subio al bus")

    def offboard(self):
        self.passengers.pop()

class Person:
    def __init__(self, name):
        self.name=name
        
        
        
        


person_1=Person("Wilson")
person_2=Person("Cindy")
person_3=Person("Kendy")
my_bus=Bus()
my_bus.onboard(person_1)
my_bus.onboard(person_2)
my_bus.onboard(person_3)
my_bus.offboard()
my_bus.onboard(person_3)







