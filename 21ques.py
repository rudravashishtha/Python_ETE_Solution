# Question 21

# (b)

import numpy as np

# Create a 2-dimensional array
arr = np.array([[1, 2, 3],
                [1, 2, 3],
                [4, 5, 6]])

# Compute row-wise counts of all possible values
unique_values, counts = np.unique(arr, return_counts=True, axis=0)

# Print the results
print("Unique values:\n", unique_values)
print("Counts:", counts)
