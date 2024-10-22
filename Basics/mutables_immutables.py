"""Mutables vs Immutables
Mutable: Objects whose values can be changed after creation.
Immutable: Objects whose values cannot be changed after creation. Any attempt to modify an immutable object results in the creation of a new object.

Common Mutable Data Types: Lists, Dictionaries, Sets
Common Immutable Data Types: Integers, Floats, Strings, Tuples, Booleans"""

# 1. Immutable Example: Integer
x = 10
print("Original Integer:", x)

x = x + 5  # This creates a new integer object, doesn't modify the original
print("Modified Integer (new object):", x)

# 2. Immutable Example: String
string = "Hello"
print("Original String:", string)

# Strings are immutable, so concatenation creates a new string object
string = string + " World"
print("Modified String (new object):", string)

# 3. Mutable Example: List
my_list = [1, 2, 3]
print("Original List:", my_list)

# Lists are mutable, so this modifies the original list
my_list.append(4)
print("Modified List (same object):", my_list)

# 4. Mutable Example: Dictionary
my_dict = {"name": "Alice", "age": 25}
print("Original Dictionary:", my_dict)

# Dictionaries are mutable, so this modifies the original dictionary
my_dict["age"] = 26
print("Modified Dictionary (same object):", my_dict)

# 5. Immutable Example: Tuple
my_tuple = (1, 2, 3)
print("Original Tuple:", my_tuple)

# Tuples are immutable, so attempting to modify a tuple will throw an error
# Uncommenting the line below will cause a TypeError
# my_tuple[0] = 10

# If you need a modified tuple, you need to create a new one
new_tuple = my_tuple + (4, 5)
print("New Tuple (new object):", new_tuple)

# 6. Mutable Example: Set
my_set = {1, 2, 3}
print("Original Set:", my_set)

# Sets are mutable, so you can add elements to them
my_set.add(4)
print("Modified Set (same object):", my_set)
