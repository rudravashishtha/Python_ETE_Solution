# Question 29

# (a)
def printTable(num):
    print(f"Multiplication table of {num}:")
    for i in range(1, 11):
        print(f"{num} * {i} = {num*i}")

number = int(input("Enter a number: "))
printTable(number)

# (b)
str = "Python is a wonderful Language"
reversed_string = str[::-1]
print("Reverse String:", reversed_string)

