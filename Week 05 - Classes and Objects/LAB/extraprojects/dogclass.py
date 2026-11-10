class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(self.name, "says Woof!")

    def birthday(self):
        self.age += 1

dog = Dog("Buddy", 3)

dog.bark()
dog.birthday()
dog.birthday()m

print("New age:", dog.age)
