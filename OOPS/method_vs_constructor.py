'''Methods: Functions defined inside a class that operate on the objects of that class. 
Methods can be called on an object to perform actions.

Constructors: Special methods (like __init__) used to initialize new objects of a class. 
They set up the initial state of the object.'''

class Animal:
    def __init__(self, species):
        self.species = species  # Constructor

    def make_sound(self):  # Method
        print(f"The {self.species} makes a sound.")

# Creating an object
my_animal = Animal("dog")
my_animal.make_sound()  # Output: The dog makes a sound.
