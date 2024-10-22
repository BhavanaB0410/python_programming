my_dict = {
    "name": "Alice",
    "age": 30
}

# Membership test
has_name = "name" in my_dict          # True
has_height = "height" not in my_dict   # True

print(f"Does the dictionary have 'name'? {has_name}")
print(f"Does the dictionary not have 'height'? {has_height}")
