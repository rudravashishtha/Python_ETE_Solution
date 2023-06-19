# Question 31

# (a)
tuple1 = tuple(input("Enter for the first tuple (comma-sep): ").split(","))
tuple2 = tuple(input("Enter for the second tuple (comma-sep): ").split(","))

# Concatenating the two tuples
concatenated_tuple = tuple1 + tuple2
print("Concatenated Tuple:", concatenated_tuple)

# (b)
my_tuple = tuple(input("Enter elements for the tuple (comma-separated): ").split(","))

element_to_check = input("Enter the element to check: ")

# Checking membership using the 'in' operator
if element_to_check in my_tuple:
    print("Element is present in the tuple.")
else:
    print("Element is not present in the tuple.")
    
    
# (c)
tuple3 = tuple(input("Enter elements for the tuple (comma-separated): ").split(","))

index = int(input("Enter the index to add the element: "))
value = input("Enter the element to add: ")

if index >= 0 and index <= len(tuple3):
    updated_tuple = tuple3[:index] + (value,) + tuple3[index:]
    print("Updated Tuple:", updated_tuple)
else:
    print("Error: Index is out of range.")

