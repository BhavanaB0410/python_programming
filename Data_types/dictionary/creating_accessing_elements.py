'''You can create a dictionary using curly braces {} or the dict() constructor. 
Access elements using their keys.
'''
# Creating a dictionary
person = {
    "name": "Bob",
    "age": 25,
    "city": "Los Angeles"
}

# Accessing elements
name = person["name"]       # 'Bob'
age = person["age"]         # 25
city = person.get("city")   # 'Los Angeles'

print(f"Name: {name}, Age: {age}, City: {city}")
