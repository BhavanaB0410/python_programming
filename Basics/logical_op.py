# Logical Operators Example

x = 10
y = 5

# 1. Logical AND
# Both conditions need to be true for the result to be True
result = (x > 5 and y < 10)
print("Logical AND (x > 5 and y < 10):", result)  # True

# 2. Logical OR
# At least one of the conditions needs to be true for the result to be True
result = (x > 5 or y > 10)
print("Logical OR (x > 5 or y > 10):", result)  # True

# 3. Logical NOT
# Reverses the result, True becomes False, and False becomes True
result = not (x > 5)
print("Logical NOT (not (x > 5)):", result)  # False

# 4. Combining multiple logical operators
result = (x > 5 and y < 10) or (x == y)
print("Combined logical expression ((x > 5 and y < 10) or (x == y)):", result)  # True
