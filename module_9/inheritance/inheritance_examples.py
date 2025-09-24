class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Some generic animal sound.")

    def description(self):
        print(f"This is an animal named {self.name}.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        print("HAAAAM HAAAAAM")

    def description(self):
        super().description()
        print(f"Breed: {self.breed}")

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def sound(self):
        print("MOOOOOOOOOOOOOOOOO")

    def description(self):
        super().description()
        print(f"Color: {self.color}")



animal = Animal("Generic Animal")
animal.sound()
animal.description()

dog = Dog("Rex", "German Shepherd")
dog.sound()
dog.description()

cat = Cat("Cat", "Black")
cat.sound()
cat.description()