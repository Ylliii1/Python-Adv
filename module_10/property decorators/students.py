class Student:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

student1 = Student("Alice", 17)

print("Name: ", student1.name)
print("Age: ", student1.age)

student1.name = "bob"
student1.age = 19

print("Updated name: ", student1.name)
print("Updated Age: ", student1.age)