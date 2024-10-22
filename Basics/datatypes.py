# Example of different data types in Python

# 1. Integer
integer_variable = 42
print("Integer:", integer_variable)

# 2. Float
float_variable = 3.14
print("Float:", float_variable)

# 3. String
string_variable = "Hello, World!"
print("String:", string_variable)

# 4. Boolean
boolean_variable = True
print("Boolean:", boolean_variable)

# 5. List (mutable)
list_variable = [1, 2, 3, 4, 5]
print("List:", list_variable)

# Adding an item to the list
list_variable.append(6)
print("Updated List:", list_variable)

# 6. Tuple (immutable)
tuple_variable = (1, 2, 3)
print("Tuple:", tuple_variable)

# 7. Set (unordered collection of unique items)
set_variable = {1, 2, 3, 3, 4, 5}  # Duplicates will be removed
print("Set:", set_variable)

# 8. Dictionary (key-value pairs)
dictionary_variable = {
    "name": "Alice",
    "age": 30,
    "height": 5.5
}
print("Dictionary:", dictionary_variable)

# Accessing a value from the dictionary
print("Name from Dictionary:", dictionary_variable["name"])

# 9. None Type
none_variable = None
print("None Type:", none_variable)
