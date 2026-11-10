class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Alice", 19)
student2 = Student("Bob", 20)

print(student1.name, student1.age)
print(student2.name, student2.age)