# Positional Arguments
def add(a, b):
    return a + b

print(add(5, 3))  # Output: 8

# Keyword Arguments
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

introduce(age=25, name="Bob")

# Default Arguments
def power(base, exponent=2):
    return base ** exponent

print(power(3))      # Output: 9 (uses default exponent)
print(power(3, 3))   # Output: 27

# Variable-length Arguments
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4, 5))  # Output: 15

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")
