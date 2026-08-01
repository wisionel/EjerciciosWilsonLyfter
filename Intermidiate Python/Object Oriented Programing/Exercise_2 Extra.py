class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        sound="Hace un sonido"
        print(sound)
        return(sound)

class Dog(Animal):
    def speak(self):
        sound="Guau"
        print(sound)
        return sound

class Cat(Animal):
    def speak(self):
        sound="Miau"
        print(sound)
        return sound

cat1=Cat("Chasiu")
dog1=Dog("Tai")
animal=Animal("Sam")
cat1.speak()
dog1.speak()
animal.speak()