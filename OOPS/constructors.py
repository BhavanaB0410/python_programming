'''
Initialize instance variables.
Set up any required properties for the object upon creation.
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating an object with constructor
person1 = Person("Alice", 30)
print(person1.name)  # Output: Alice
print(person1.age)   # Output: 30
