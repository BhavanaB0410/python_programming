"""implicit and explicit type convertions
converting lower to higher"""
# Example of type conversions in Python

# 1. Integer to Float
integer_value = 42
float_value = float(integer_value)
print("Integer to Float:", float_value)

# 2. Float to Integer
float_value = 3.14
integer_value = int(float_value)  # Truncates the decimal part
print("Float to Integer:", integer_value)

# 3. String to Integer
string_value = "100"
integer_value = int(string_value)
print("String to Integer:", integer_value)

# 4. String to Float
string_value = "3.14159"
float_value = float(string_value)
print("String to Float:", float_value)

# 5. Integer to String
integer_value = 42
string_value = str(integer_value)
print("Integer to String:", string_value)

# 6. Float to String
float_value = 3.14
string_value = str(float_value)
print("Float to String:", string_value)

# 7. List to Tuple
list_value = [1, 2, 3]
tuple_value = tuple(list_value)
print("List to Tuple:", tuple_value)

# 8. Tuple to List
tuple_value = (1, 2, 3)
list_value = list(tuple_value)
print("Tuple to List:", list_value)

# 9. String to List
string_value = "Hello"
list_value = list(string_value)  # Converts each character to a list element
print("String to List:", list_value)

# 10. List to String
list_value = ['H', 'e', 'l', 'l', 'o']
string_value = ''.join(list_value)  # Joins list elements into a single string
print("List to String:", string_value)
