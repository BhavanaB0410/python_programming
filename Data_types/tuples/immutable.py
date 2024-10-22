my_tuple = (1, 2, 3)

# Trying to change an element (this will raise an error)
try:
    my_tuple[1] = 4  # Attempting to modify the second element
except TypeError as e:
    print(f"Error: {e}")
