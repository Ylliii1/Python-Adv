class Rectangle:
    def __int__(self,width,length):
        self.width = width
        self.length = length
    def calculate_area (self):
        return self.length * self.width
    def











class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, iam {self.name}, and iam {self.age} old")

person1 = Person("John", 16)
person2 = Person("Joe", 17)

person1.greet()
person2.greet()





class Student:
    school_name = "Digital School"

    def __init__(self,name,age,course):
        self.name = name
        self.age = age
        self.course = course

student1 = Student("John", 16, 'Python')
student2 = Student("Joe", 17, 'Python')

print(student1.age)








