# Question 40

import numpy as np

def cube(x):
    return x ** 3

# cube_func = np.vectorize(cube)

arr = np.array([1, 2, 3, 4, 5])

result = cube(arr)
print("Result:", list(result))

