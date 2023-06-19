# Question 44
import re

def contains_only(string):
    pattern = r'^[a-zA-Z0-9]+$'
    match = re.match(pattern, string)
    return match is not None

test_string1 = "Hello123"
test_string2 = "Hello123!"
test_string3 = "1234567890"
test_string4 = "!@#$%^&*"

print(contains_only(test_string1))
print(contains_only(test_string2))
print(contains_only(test_string3))
print(contains_only(test_string4))
