# Membership Operators Example

# Define some sequences
my_list = [1, 2, 3, 4, 5]
my_string = "Hello, world!"
my_tuple = ('a', 'b', 'c')

# 1. 'in' Operator
# Check if an element is in a list
result = 3 in my_list
print("Is 3 in my_list?", result)  # True

# Check if a character is in a string
result = 'H' in my_string
print("Is 'H' in my_string?", result)  # True

# Check if an element is in a tuple
result = 'd' in my_tuple
print("Is 'd' in my_tuple?", result)  # False

# 2. 'not in' Operator
# Check if an element is not in a list
result = 6 not in my_list
print("Is 6 not in my_list?", result)  # True

# Check if a substring is not in a string
result = "Python" not in my_string
print("Is 'Python' not in my_string?", result)  # True
