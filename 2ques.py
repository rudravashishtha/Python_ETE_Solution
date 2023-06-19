# Question 2

import random

# Set the seed
print("For seed 2")
random.seed(2)
for i in range(5):
    print(random.randint(1, 10), end=" ")

print("\nFor seed 4")
random.seed(4)
for i in range(5):
    print(random.randint(1, 10), end=" ")
    
# Re-run the program with the same seed
print("\nFor seed 2")
random.seed(2)
for i in range(5):
    print(random.randint(1, 10), end=" ")

print("\nFor seed 4")
random.seed(4)
for i in range(5):
    print(random.randint(1, 10), end=" ")
