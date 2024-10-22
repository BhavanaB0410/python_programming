'''You can remove elements from a set using remove(), discard(), or pop(). 
The remove() method raises an error if the element does not exist, while discard() does not.'''
my_set = {1, 2, 3, 4}

# Removing an element (will raise KeyError if not found)
my_set.remove(3)

# Discarding an element (will not raise an error if not found)
my_set.discard(5)  # Does nothing

# Pop an element (removes and returns an arbitrary element)
popped_element = my_set.pop()  # Random element is removed

print(f"Remaining set: {my_set}")
print(f"Popped element: {popped_element}")
