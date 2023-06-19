# Question 36

# (a)

a = input("Enter a: ")
b = input("Enter b: ")

def add(a, b):
    return a+b

print("Result:", add(a, b))

# (b)

def simplecalc(a, b):
    addition = a+b
    substraction = a-b
    multiplication = a*b
    print("Addition:", addition,
          "Substraction:", substraction,
          "Multiplication:", multiplication)

a = 3
b = 4
print("Operations in regular order")
simplecalc(a, b)
print("Operations in reverse order")
simplecalc(b, a)

