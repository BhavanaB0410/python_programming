

set_a = {1, 2, 3}
set_b = {3, 4, 5}

# Union
union_set = set_a | set_b  # {1, 2, 3, 4, 5}

# Intersection
intersection_set = set_a & set_b  # {3}

# Difference
difference_set = set_a - set_b  # {1, 2}

# Symmetric Difference
symmetric_difference_set = set_a ^ set_b  # {1, 2, 4, 5}

print(f"Union: {union_set}")
print(f"Intersection: {intersection_set}")
print(f"Difference: {difference_set}")
print(f"Symmetric Difference: {symmetric_difference_set}")
