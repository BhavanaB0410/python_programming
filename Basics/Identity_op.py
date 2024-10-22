""" IDENTITY Operator
is: This operator checks if two variables point to the same object in memory.
is not: This operator checks if two variables do not point to the same object in memory."""

a = [1, 2, 3]
b = a  # b points to the same list object as a
c = [1, 2, 3]  # c is a new list object with the same content as a

print(a is b)  # Output: True, since b is referencing the same object as a
print(a is c)  # Output: False, since c is a different object in memory


print(a is not b)  # Output: False, since b is referencing the same object as a
print(a is not c)  # Output: True, since c is a different object in memory
