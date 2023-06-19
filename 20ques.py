# Question 20

# (a) The number must be divisible by five
# (b) If the number is greater than 150, then skip it and move to the next number
# (c) If the number is greater than 500, then stop the loop
# (d) Input: numbers = [12, 75, 150, 180, 145, 525, 50]
# (e) Output:
# 75
# 150
# 145

arr = [12, 75, 150, 180, 145, 525, 50]

for num in arr:
    if num % 5 == 0:
        if num > 500:
            break
        elif num % 5 == 0 and num <= 150:
            print(num)

