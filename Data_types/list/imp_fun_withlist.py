"""Python provides several built-in functions for lists, such as append(), remove(), pop(), and sort()."""
animals = ["cat", "dog", "rabbit"]

# Append
animals.append("hamster")  # ['cat', 'dog', 'rabbit', 'hamster']

# Remove
animals.remove("dog")      # ['cat', 'rabbit', 'hamster']

# Pop
popped_animal = animals.pop()  # Removes and returns 'hamster'

# Sort
animals.sort()  # Sorting the remaining animals

print(f"Animals: {animals}")
print(f"Popped animal: {popped_animal}")
