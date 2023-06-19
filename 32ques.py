# Question 32

print("--a--")
original_dict = {"20": "Age", "Banana": "Fruit", "Carrot": "Vegetable"}
print("Original Dictionary:")
print(original_dict)

swapped_dict = {}
for key, value in original_dict.items():
    key, value = value, key
    swapped_dict[key] = value

print("Swapped Dictionary:")
print(swapped_dict)

print("\n--b--")
def create_frequency_dict(sequence):
    frequency_dict = {}
    for element in sequence:
        if element in frequency_dict:
            frequency_dict[element] += 1
        else:
            frequency_dict[element] = 1
    return frequency_dict

sequence = list(map(int, input("Enter an integer sequence (space-separated): ").split()))
frequency_dict = create_frequency_dict(sequence)
print("Frequency Dictionary:")
for key, value in frequency_dict.items():
    print(key, ":", value)

