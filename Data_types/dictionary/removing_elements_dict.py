my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Using del
del my_dict["age"]  # Removes the 'age' key-value pair

# Using pop()
city = my_dict.pop("city")  # Removes and returns 'city'

print(f"Remaining dictionary: {my_dict}")
print(f"Removed city: {city}")
