# List
my_list = [1, 2, 3]
my_list[0] = 10  # Allowed

# Tuple
my_tuple = (1, 2, 3)
try:
    my_tuple[0] = 10  # Not allowed, will raise TypeError
except TypeError as e:
    print(f"Error: {e}")
