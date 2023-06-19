# Question 10

def getresult(percentage):
    print("Result:")
    if percentage >= 70:
        print("Distinction")
    elif percentage >= 60 and percentage <= 69:
        print("Merit")
    elif percentage >= 40 and percentage <= 59:
        print("Pass")
    else:
        print("Fail")

while True:
    percentage = int(input("Enter the percentage: "))
    if percentage > 0 and percentage <= 100:
        getresult(percentage)
