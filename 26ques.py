# Question 26
# Method 1
def is_palindrome1(num):
    num_str = str(num)
    if num_str == num_str[::-1]:
        return True
    else:
        return False

# Method 2
def is_palindrome2(num):
    original_number = num
    reverse = 0
    while num > 0:
        last_digit = num % 10
        reverse = reverse * 10 + last_digit
        num //= 10
    if original_number == reverse:
        return True
    else:
        return False
        
number = int(input("Enter a number: "))
if is_palindrome1(number):
    print("Using 1: Number is palindrome")
if is_palindrome2(number):
    print("Using 2- Number is Palindrome")
else:
    print("Number is not Palindrome")

