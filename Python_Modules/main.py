# main.py

import mymodule  # Import the custom module

result_add = mymodule.add(5, 3)
result_subtract = mymodule.subtract(5, 3)

print(f"Addition: {result_add}")        # Output: Addition: 8
print(f"Subtraction: {result_subtract}") # Output: Subtraction: 2

'''Python Modules: Files containing Python code that can define functions, classes, and variables.
Purpose: To promote code reusability, organization, avoid name clashes, and support collaboration.
Creating: Write functions/classes in a .py file.
Using: Import the module using import or from ... import statements.
'''