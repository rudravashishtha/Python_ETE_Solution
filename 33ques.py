# Question 33

# Adding
my_dict1 = {}
my_dict1["name"] = "John"
my_dict1["age"] = 25
print(my_dict1)

# Updating
dict2 = {"a": 1, "b": 2}
dict3 = {"c": 3, "d": 4}
dict3.update(dict2)
print(dict3)

# Removing Method1
my_dict4 = {"name": "John", "age": 26}
removed_value = my_dict4.pop("age")
print("After Removed:", my_dict4)
print("Removed Value:", removed_value)

# Removing Method2
my_dict5 = {"a": 1, "b": 2, "c": 3, "d": 4}
removed_item = my_dict5.popitem()
print("After Removed:", my_dict5)
print("Removed Item:", removed_item)

